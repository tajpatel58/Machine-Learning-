import numpy as np
from .sig import sigmoid 

def feed_forward(X, params, input_layer, hidden_layer, output_layer):
    """
    Given the model parameters and hyperparemeters, we can feed our data forward through the neural network, this
    function essentially does exactly that. However it doesn't obtain a prediction at the end of the feed forward process.
    It merely outputs the matrix of probabilities. 

    Parameters:
        X (numpy array): Matrix whose rows are different data entries, which we want to feed forward. 
        params (numpy array): Unrolled vector of weights that we want to use to feed forward.
        input_layer (int): Integer size of the input layer. 
        hidden_layer (int): Integer size of the hidden layer of the Neural Network. 
        output_layer (int): Integer size of the output layer.
    
    Returns: 
        a_3 (numpy array): Array of probabilities. If we feed forward m pieces of data, then the output is
                           a mx10 matrix, where the j^{th} entry is the probability that this data belongs is equal
                           the digit j.  
    """
    # Need to resize params as our 2 transformations between layers. Theta_1 in R^{25x401}, Theta_2 in R^{10x26}
    Theta_1 = params[:hidden_layer*(input_layer+1)].reshape(hidden_layer, input_layer+1)
    Theta_2 = params[hidden_layer*(input_layer+1):].reshape((output_layer,hidden_layer+1))

    # Can forward propagate:
    z_2 = np.matmul(X,Theta_1.T)
    a_2 = sigmoid(z_2)
    a_2 = np.insert(a_2,0, 1,axis=1)
    z_3 = np.matmul(a_2,Theta_2.T)
    a_3 = sigmoid(z_3)
    return a_3