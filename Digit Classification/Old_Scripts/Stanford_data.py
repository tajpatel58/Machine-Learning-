import scipy.io
import numpy as np
from Functions_For_Model import *
import math
from sig import sigmoid
from cost_func import cost_func 
from feed_forward import feed_forward
import scipy.optimize as op
from rand_initial_weights import rand_initial_weights
from predict import predict 
from PIL import Image 
import matplotlib.pyplot as plt

# This is a neural network used for number hand writing recoginition. The neural network in this case,
# has features given by a 20x20 pixel picture. Only one hidden layer with 25 units and ofcouse the output layer of 10.


# data is now a dictionary, look at the keys and you'll know how to get X and Y. 
data = scipy.io.loadmat('ex4data1')

# Inital weights/params used to test the cost function.
test_param = scipy.io.loadmat('ex4weights')
test_theta1 = test_param['Theta1']
test_theta2 = test_param['Theta2']

# These are the design matrix and corresponding output for the 5000 data points. (Stored as numpy arrays)
X = data['X']
y = data['y']


# Some model dimensions, m = data size, n= feature length, lambd = regularization coefficient, 
# epsilon is a value such that inital random weights for optimizer are sampled from the interval (-epsilon, epsilon).
m = X.shape[0]
n = X.shape[1] + 1 
k = 10 #(number of classes)
lambd = 1
pixel_dim = 20
input_layer = 400
hidden_layer = 25
output_layer = 10
epsilon = 0.1

# need to add a column of 1's to our design matrix.


# Need to manipulate y to obtain matrix Y, Y is a matrix of 0's and 1's. Yij = 1 iff data i has value j. 
Y = np.zeros((m, k))

for j in range(1,10):
    idx = np.where(y == j)
    Y[idx[0], j-1] = 1

idx_0 = np.where(y==10)
Y[idx_0[0],9] = 1 


# Need a vector/list input for minimisation. 
params = np.hstack((test_theta1.reshape(1,hidden_layer*(input_layer+1)), test_theta2.reshape(1,output_layer*(hidden_layer+1))))
params = params.flatten()


# Need to train the Netural Network, (obtain parameters that minimise cost):

cost = lambda p: cost_func(X,Y,p,lambd, input_layer, hidden_layer, output_layer)[0]

grad = lambda p: cost_func(X,Y,p,lambd, input_layer, hidden_layer, output_layer)[1]

# generate initial random weights:
initial_Theta1_vec = rand_initial_weights(epsilon,input_layer,hidden_layer)
initial_Theta2_vec = rand_initial_weights(epsilon, hidden_layer,output_layer)
initial_param = np.hstack((initial_Theta1_vec, initial_Theta2_vec))
initial_param = initial_param.flatten()

# Optional argument whether to run the ML algorithm, can also use the default params. 
optimize = 0
if optimize:    
    params = op.fmin_cg(cost, initial_param, fprime=grad,maxiter = 50)

# Using model_predictions, and add one due each prediction due to the fact class 0 had label 10 (training data), here
# we generate the predictions for the training data. Need to add one based upon the indexxing in python. 
model_predictions = predict(X, params, input_layer, hidden_layer, output_layer).reshape((m,1)) 

rand_num = np.random.randint(0, m-1, 20)

# Now we will try to load some of our own handwritten examples and see if the model can determine what number we've drawn
# need to apply some preprocessing to our figure.  Can use: https://kleki.com to draw our numbers. 
image = Image.open('test_9_2.png')
grayscale_img = image.convert(mode='L')
grayscale_img = grayscale_img.resize((pixel_dim,pixel_dim))
pixel_image = np.invert(np.asarray(grayscale_img)).T
data_image = pixel_image.reshape((1,pixel_dim*pixel_dim))/255
data_image = np.insert(data_image, 0, 1, axis=1)

# r is a parameter chosen from 0-4999, to pick the index of the test_data that we want to depict. 
r = 4700
test_data = X[r,1:].reshape((pixel_dim, pixel_dim)).T
test_vec = X[r,1:]

# Print out what the model predicts the number to be. 
print(predict(data_image, params, input_layer, hidden_layer, output_layer))

# Plot pixel picture of the r^{th} data point, set ind to True. 
ind = True
if ind:
    fig = plt.figure(1)
    plt.imshow(test_data, cmap='gray_r')

# Plot pixel picture of our own data. 
fig2 = plt.figure(2)
plt.imshow(pixel_image.T/255, cmap='gray_r')

# Print accuracy on training data:
model_accuracy = (y==model_predictions).sum()/m * 100
print("The model Accuracy is:"+" "+str(model_accuracy)+"%")

plt.show()

