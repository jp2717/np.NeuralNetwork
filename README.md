# np.NeuralNetwork
A practice project that takes a neural network that learns multiclass classfication with the MNIST dataset in PyTorch and implements it in Numpy and other relevant libraries:

In order to implement this Neural network, the PyTorch implementation is shown in 'nn_pytorch.ipynb' for comparison.

Things to be implemented:
1. Main junypter notebook where different functions are carried out to use the NN model created
2. Function that loads in the MNIST dataset (without using PyTorch)
3. Function that splits dataset into training, validation and test data
4. Function that splits a given dataset into batches of a given input batch size
5. Linear layer class that takes in the number of inputs and outputs of the given layer, with a call method to pass data through it
6. Non-linear activation function applied at the end of each forward pass of a layer (RELU in this case)
7. Neural Network class that takes in linear layer objects as attributes and contains its own forward method
8. Create a loss class that takes the predictions and labels as inputs, and includes a cross entropy loss call method and a backpropagation method (contains a NxN matrix of zeros to store gradients for backprop). Also include a reset method.
9. Function that trains a given instance of our model given the appropriate input
10. Function that tests a given model for a given dataset and outputs the given accuracy of that model 
11. Function that plots the evolution of all weights of a given layer given the number of iterations of training
