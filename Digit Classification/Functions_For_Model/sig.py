import numpy as np

# sigmoid function: used as activation function.
def sigmoid(x):
    """
    Sigmoid function g(x) = 1/(1+np.exp(-x)), essentially a method used to apply the sigmoid function elementwise
    to array and matrices. 

    Parameters: 
        x (float, numpy array): Matrix/value that we want to apply the sigmoid function elementwise. 

    Returns:
        values(float, numpy array): A float or array of sigmoid applied elementwise. 

    """
    values = 1/(1+np.exp(-x))
    return values


def sigmoid_grad(x):
    """
    Evaluate the gradient of the sigmoid at the point x. 

    Parameters: 
        x (float, numpy array): Matrix/value that we want to apply the gradient of the sigmoid function elementwise. 

    Returns 
        grad (float, numpy array): Value/Values corresponding to the gradient applied elementwise. 
    """
    grad = np.multiply(sigmoid(x),(1-sigmoid(x)))
    return grad 