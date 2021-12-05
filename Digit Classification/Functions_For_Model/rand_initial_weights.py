import numpy as np

def rand_initial_weights(epsilon, layer_in, layer_out):
    # random initialise the weights/ parameters from going from one layer to the other. 
    # each parameter in the model will be uniformly obtained from the interval: (-epsilon, epsilon)

    # output is in a list format, should reshape if wanting to use as matrix. 
    return np.random.uniform(-epsilon, epsilon, (layer_in+1) * layer_out).reshape(1,(layer_in+1) * layer_out)