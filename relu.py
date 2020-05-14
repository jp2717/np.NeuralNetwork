#Simple implementation of relu of a vector

import numpy as np
#Input: data vector as numpy array
#Output: relu non-linear output vector as numpy array

def relu(data):
    return np.array([ np.maximum(val,0) for val in np.nditer(data)])

#Code test:
# a = np.array([1,2,-4,-2,5])
# print(relu(a))