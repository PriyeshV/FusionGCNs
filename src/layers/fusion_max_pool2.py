import tensorflow as tf
from src.layers.layer import Layer
from src.utils.inits import glorot, tanh_init, identity


class Fusion(Layer):

    def __init__(self, n_layers, x_names, input_dim, output_dim, dropout, bias,  act=lambda x: x,**kwargs):
        super(Fusion, self).__init__(**kwargs)
        self.n_layers = n_layers + 1
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.act = act
        self.dropout = dropout
        self.node_features = x_names[0]
        self.neighbor_features = x_names[1]
        self.bias = bias

        self.start_h = 0
        # self.fusion_dim = self.output_dim
        self.fusion_dim = self.input_dim
        for i in range(self.start_h, self.n_layers):
            self.vars['weights_' + str(i)] = glorot((self.input_dim, self.fusion_dim), name='weights_' + str(i))

    def _call(self, inputs):
        # outputs = []
        # for i in range(self.start_h, self.n_layers):
        #     print('Fusion input:', i+1)
        #     data = inputs['activations'][i+1]
        #     data = tf.nn.dropout(data, 1 - self.dropout)
        #     data = tf.matmul(data, self.vars['weights_'+str(i)])
        #     outputs.append(data)

        # added additionally
        outputs = inputs['activations'][1:]

        outputs = tf.stack(outputs, axis=2)
        outputs = tf.reduce_max(outputs, axis=2)
        return outputs
