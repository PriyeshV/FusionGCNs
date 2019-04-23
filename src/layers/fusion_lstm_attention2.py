import tensorflow as tf
from src.layers.layer import Layer
from src.utils.inits import glorot

#TODO:
#   - Activation of each layer before fusion
#   - Dimensions
#   - Mean vs sum


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

        self.fusion_dim = self.output_dim

        self.start_h = 0
        self.lstm_fw_cell = tf.nn.rnn_cell.LSTMCell(self.fusion_dim, forget_bias=1.0)
        self.lstm_bw_cell = tf.nn.rnn_cell.LSTMCell(self.fusion_dim, forget_bias=1.0)

        self.vars['weights_att'] = glorot((self.fusion_dim*2, 1), name='weights_A')


    def _call(self, inputs):
        outputs = []
        for i in range(self.start_h, self.n_layers):
            print('Fusion input:', i+1)
            data = tf.reshape(inputs['activations'][i+1], [-1, self.input_dim])
            outputs.append(data)

        rnn_outputs, out_fw, out_bw = tf.nn.static_bidirectional_rnn(self.lstm_fw_cell, self.lstm_bw_cell, outputs, dtype=tf.float32)
        attention_score = tf.nn.softmax(tf.contrib.slim.fully_connected(rnn_outputs, 1))
        rnn_outputs = tf.multiply(rnn_outputs, attention_score)
        outputs = tf.reduce_sum(rnn_outputs, axis=0)
        # outputs = self.act(outputs)
        return outputs