import numpy as np
from .sig import sigmoid 

def feed_forward(X, params, input_layer, hidden_layer, output_layer):

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