import tensorflow as tf
from src.layers.layer import Layer
from src.utils.inits import glorot, tanh_init, identity

#TODO: Binomial attention
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
        # self.fusion_dim = 128
        self.fusion_dim = self.output_dim

        self.start_h = 0
        # if len(self.node_features) == 0 and self.m_name no:
        #     self.start_h += 1

        # self.fusion_dim = self.output_dim
        self.fusion_dim = self.input_dim

        for i in range(self.start_h, self.n_layers):
            self.vars['weights_'+str(i)] = glorot((self.input_dim, self.fusion_dim), name='weights_'+str(i))
        # self.vars['weights_final'] = identity((self.fusion_dim, self.output_dim), name='weights_final')
        self.vars['weights_final'] = identity((self.fusion_dim, self.fusion_dim), name='weights_final')

        # Matrix gating
        self.vars['weights_A'] = identity((self.fusion_dim, self.fusion_dim), name='weights_A')

        # Triple vector Gating
        gate_dim = self.fusion_dim
        self.vars['weights_C'] = identity((self.fusion_dim, gate_dim), name='weights_C')
        self.vars['weights_D'] = identity((self.fusion_dim, gate_dim), name='weights_D')
        self.vars['weights_V'] = tanh_init((1, gate_dim), name='weights_V')

        self.vars['weights'] = glorot((self.fusion_dim, self.output_dim), name='weights_final2')

    def reduce_sum_attsop(self, x):
        return tf.matmul(x, tf.ones([self.fusion_dim, 1]))

    def _call(self, inputs):
        outputs = []
        for i in range(self.start_h, self.n_layers):
            print('Fusion input:', i+1)
            data = inputs['activations'][i+1]
            data = tf.nn.dropout(data, 1 - self.dropout)
            data = tf.matmul(data, self.vars['weights_'+str(i)])
            outputs.append(data)

        attention_score = tf.contrib.slim.fully_connected(outputs, 1)
        outputs = tf.multiply(outputs, attention_score)
        outputs = tf.reduce_sum(outputs, axis=0)
        outputs = tf.nn.l2_normalize(outputs, dim=1)

        outputs = self.act(outputs)
        outputs = tf.matmul(outputs, self.vars['weights'])
        return outputs

        # Attention score:= tanh [W_V * ( Context * W_C + D * W_D)]
        # context = 0
        # for i in range(self.start_h, self.n_layers):
        #     context += outputs[i]
        # context /= (self.start_h - self.n_layers)
        # context = tf.matmul(context, self.vars['weights_C'])
        #
        # outs = 0
        # for i in range(self.start_h, self.n_layers):
        #     temp = tf.matmul(outputs[i], self.vars['weights_D']) + context
        #     score = self.reduce_sum_attsop(tf.multiply(temp, self.vars['weights_V']))
        #     score = tf.nn.tanh(score)
        #     outs += score*outputs[i]
        #
        # outs = tf.matmul(outs / (self.n_layers - self.start_h), self.vars['weights_final'])
        # outputs = self.act(outs)

        # added additionally
        # outputs = tf.matmul(outputs, self.vars['weights'])
        # return outputs