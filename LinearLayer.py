import numpy as np

#Class that helps create linear layer instances with the desired properties we want

class LinearLayer:

    def __init__(self,n_inputs,n_outputs):
        self.n_inputs = n_inputs #number of features of one sample
        self.n_outputs = n_outputs #number of outputs generated from one example
        self.weights = np.zeros((n_outputs,n_inputs)) #number of inputs as columns and desired outputs as rows
        self.bias = np.random.randn(n_outputs) #biases added to each output of the layer

    def get_weights(self):
        return self.weights
    def get_n_inputs(self):
        return self.n_inputs
    def get_n_outputs(self):
        return self.n_outputs
    def __call__(self,X): #takes input of length n_inputs and passes through model
        layer_output = np.matmul(self.weights,np.transpose(X)) + self.bias #linear combination with additive bias
        return layer_output
    def update_params(self,new_weights,new_bias):
        self.weights = new_weights
        self.bias = new_bias

#Code test:
# layer = LinearLayer(10,8)
# print(layer.get_weights())