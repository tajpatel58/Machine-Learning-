import scipy.io
import numpy as np
import tensorflow 
import math
from sig import sigmoid
from cost_func import cost_func 
from feed_forward import feed_forward
import scipy.optimize as op
from rand_initial_weights import rand_initial_weights
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt 
from predict import predict

# Neural Network for the MNIST data with one input layer(given by 28x28 gray scale pixel pictures), one hidden layer
# and one output layer. We use Tensorflow only to import the dataset, the rest is coded from scratch as an exercise
# in implementing a netural network. 


# Load the MNIST training data. 
(train_X, train_y), (test_X, test_Y) = mnist.load_data()

# Will use the first 5000 examples for training. 
m = 5000

# We shall only use the first 5000 pieces of data.
train_X = train_X[:m, :,:]
train_y = train_y[:m]

# Some code to visualise the data. 
sample_num = 0
image = train_X[sample_num,:,:]
fig = plt.figure
plt.imshow(image, cmap='gray_r')
plt.show()

# Pre-process so that the rows of design matrix correspond to the different pixel intensities. 
X = tensorflow.reshape(train_X,[m, 28*28])

# Some model dimensions
n = X.shape[1] + 1 
k = 10 #(number of classes)
lambd = 1
input_layer = 28*28
hidden_layer = 25
output_layer = 10
epsilon = 0.1

# Add columns of 1's. (bias)
X = np.insert(X, 0, 1,axis = 1)

# Pre-process the data to form the label matrix, y_i,j = 1 iff data point i takes value j. 
Y = np.zeros((m, k))

for i in range(0,10):
    idx = np.where(train_y == i)
    Y[idx, i] == 1

# Need to train the Neural Network, shall use fmincg from scipy to optimize the cost function. 
cost = lambda p: cost_func(X,Y,p,lambd, input_layer, hidden_layer, output_layer)[0]

grad = lambda p: cost_func(X,Y,p,lambd, input_layer, hidden_layer, output_layer)[1]

initial_Theta1_vec = rand_initial_weights(epsilon,input_layer,hidden_layer)
initial_Theta2_vec = rand_initial_weights(epsilon, hidden_layer,output_layer)
initial_param = np.hstack((initial_Theta1_vec, initial_Theta2_vec))
initial_param = initial_param.flatten()

param_opt = op.fmin_cg(cost, initial_param, fprime=grad,maxiter = 10)

model_predictions = predict(X, param_opt, input_layer, hidden_layer, output_layer)

# Randomly choose data points compare data with those predicted from our model

rand_num = np.random.randint(0, m-1, 20)

print(param_opt)

print(model_predictions[rand_num])
print(train_y[rand_num].T)



