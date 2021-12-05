import numpy as np

# sigmoid function: used as activation function.
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Sigmoid gradient used in computing the activation errors for each layer. 
def sigmoid_grad(x):
    return np.multiply(sigmoid(x),(1-sigmoid(x))) 