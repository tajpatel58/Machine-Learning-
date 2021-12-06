import numpy as np
from .feed_forward import feed_forward

# Prediction values correspond to the index of the highest probability in each row of the output matrix from the feedforward
# algorithm. We add one to the returned due to the indexxing in python. 
def predict(X, params, input_layer, hidden_layer, output_layer):
    probability_mat = feed_forward(X, params, input_layer, hidden_layer, output_layer)
    predicted_value =  np.argmax(probability_mat, axis=1) + 1 
    if predicted_value == 10:
        return 0 
    else:
        return predicted_value
