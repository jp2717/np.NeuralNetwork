#class that will actually represent our neural network model for the MNIST dataset
import numpy as np
from LinearLayer import LinearLayer

class NeuralNetwork:
    def __init__(self):
        self.layer1 = LinearLayer(784, 1024)
        self.layer2 = LinearLayer(1024,256)
        self.layer3 = LinearLayer(256,10)