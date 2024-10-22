import tensorflow as tf
import numpy as np


def identity(shape, scale=1, name=None, trainable=True):
    "Diagonal init"
    return tf.Variable(tf.eye(shape[0])*scale, name=name, trainable=trainable)


def uniform(shape, scale=0.05, name=None, trainable=True):
    """Uniform init."""
    initial = tf.random_uniform(shape, minval=-scale, maxval=scale, dtype=tf.float32)
    return tf.Variable(initial, name=name, trainable=trainable)


def glorot(shape, name=None, trainable=True):
    """Glorot & Bengio (AISTATS 2010) init."""
    # init_range = np.sqrt(6.0/(shape[0]+shape[1]))
    # initial = tf.random_uniform(shape, minval=-init_range, maxval=init_range, dtype=tf.float32)
    init_range = np.sqrt(2.0/(shape[1]))
    shape = tf.cast(shape, tf.int32)
    initial = tf.random_normal(shape, dtype=tf.float32) * init_range
    return tf.Variable(initial, name=name, trainable=trainable)


def tanh_init(shape, name=None, dtype=tf.float32, partition_info=None, trainable=True):
    init_range = np.sqrt(6.0/(shape[0]+shape[1]))
    initial = tf.random_uniform(shape, minval=-init_range, maxval=init_range, dtype=tf.float32)
    return tf.Variable(initial, name=name, trainable=trainable)


def sigmoid_init(shape, name=None, dtype=tf.float32, partition_info=None, trainable=True):
    init_range = 4*np.sqrt(6.0/(shape[0]+shape[1]))
    initial = tf.random_uniform(shape, minval=-init_range, maxval=init_range, dtype=tf.float32)
    return tf.Variable(initial, name=name, trainable=trainable)


def zeros(shape, name=None, trainable=True):
    """All zeros."""
    initial = tf.zeros(shape, dtype=tf.float32)
    return tf.Variable(initial, name=name, trainable=trainable)


def const(shape, val=0.1, name=None, trainable=True):
    initial = tf.constant(val, shape=shape, dtype=tf.float32)
    return tf.Variable(initial, name=name, trainable=trainable)


def ones(shape, name=None, trainable=True):
    """All ones."""
    initial = tf.ones(shape, dtype=tf.float32)
    return tf.Variable(initial, name=name, trainable=trainable)


def orthogonal(shape):
    flat_shape = (shape[0], np.prod(shape[1:]))
    a = np.random.normal(0.0, 1.0, flat_shape)
    u, _, v = np.linalg.svd(a, full_matrices=False)
    q = u if u.shape == flat_shape else v
    return q.reshape(shape)


def orthogonal_initializer():
    def _initializer(shape, dtype=tf.float32, partition_info=None):
        return tf.constant(orthogonal(shape), dtype)
    return _initializer


def bn_lstm_identity_initializer(scale):
    def _initializer(shape, dtype=tf.float32, partition_info=None):
        '''Ugly cause LSTM params calculated in one matrix multiply'''
        size = shape[0]
        # gate (j) is identity
        t = np.zeros(shape)
        t[:, size:size * 2] = np.identity(size) * scale
        t[:, :size] = orthogonal([size, size])
        t[:, size * 2:size * 3] = orthogonal([size, size])
        t[:, size * 3:] = orthogonal([size, size])
        return tf.constant(t, dtype)

    return _initializer