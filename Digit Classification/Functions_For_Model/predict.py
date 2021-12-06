import numpy as np
from .feed_forward import feed_forward

# Prediction values correspond to the index of the highest probability in each row of the output matrix from the feedforward
# algorithm. We add one to the returned due to the indexxing in python. 
def predict(X, params, input_layer, hidden_layer, output_layer):
    """

    Parameters: 
        X (numpy array): Matrix of data for which we want to predict which digit each row corresponds to. 
        params (numpy array): Unrolled vector of weights, used to predict digit. 
        input_layer (int): Integer size of the input layer. 
        hidden_layer (int): Integer size of the hidden layer of the Neural Network. 
        output_layer (int): Integer size of the output layer.

    Return:
        predicted_values (numpy array): An array of predictions for each data piece. In particular
                                        if we provide m rows in X, then the output is of length m. 
                                        The i^{th} row is the predicted digit for the i^{th} data point. 

    
    
    """
    probability_mat = feed_forward(X, params, input_layer, hidden_layer, output_layer)
    predicted_values =  np.argmax(probability_mat, axis=1) + 1 
    return predicted_values
