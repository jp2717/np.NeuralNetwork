# this function will create gradient objects, which contain the gradient of each parameter wrt all other parameters

import numpy as np

class Gradient:
    def __init__(self,layers): #takes in each of our layers as inputs
        #determining number of all parameters
        self.num_param = 0
        for layer in layers:
            self.num_param+= len(layer.get_weights()) + len(layer.get_bias())
        
        #stores gradient of a variable (along columns) wrt to another (along rows)
        self.grad = np.zeros((self.num_param,self.num_param))

    def get_grad(self):
        return self.grad
    def zero_grad():
        self.grad = np.zeros((self.num_param,self.num_param))

    def back():
        pass