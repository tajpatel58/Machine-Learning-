import numpy as np

def rand_initial_weights(epsilon, layer_in, layer_out):
    """
    Randomly initialise the weights/ parameters from going from one layer to the other. 
    Each model parameter is initialised by uniformly sampling from the interval: (-epsilon, epsilon)

    Parameters:
        epsilon (float): Endpoint of the interval for which we want to sample from.
        layer_in (float): Number of units on the previous layer excluding the bias. 
        layer_out (falot): Number of units on the current layer excluding the bias. 
    
    Return:
        rand_weights(numpy array): An unrolled vector of randomised model parameters for a particular layer. 
    
    """

    # output is in a list format, should reshape if wanting to use as matrix. 
    rand_weights = np.random.uniform(-epsilon, epsilon, (layer_in+1) * layer_out).reshape(1,(layer_in+1) * layer_out)
    return rand_weights