from feed_forward import feed_forward
import numpy as np
from sig import sigmoid 
from sig import sigmoid_grad

def cost_func(X, Y, params, lambd, input_layer, hidden_layer,output_layer):
    # need to return the cost and the gradient.

    Theta_1 = params[:hidden_layer*(input_layer+1)].reshape((hidden_layer,input_layer+1))
    Theta_2 = params[hidden_layer*(input_layer+1):].reshape((output_layer,hidden_layer+1))

    # need to forward propagate first, can simply call the "predict" function. 
    pred = feed_forward(X, params, input_layer, hidden_layer, output_layer)
    m = X.shape[0]

    # Implement the first term of cost
    log_pred = np.log(pred)
    neg_log_pred = np.log(1-pred)
    cost = -1/m * np.sum(np.multiply(Y, log_pred) + np.multiply(1-Y,neg_log_pred))

    # Add regularization term. 
    cost += lambd/(2*m) * (np.sum(np.square(Theta_1[:,1:])) + np.sum(np.square(Theta_2[:,1:])))


    # Default the gradient, which we will unroll once backpropogation is complete. 
    grad_1 = np.zeros(Theta_1.shape)
    grad_2 = np.zeros(Theta_2.shape)

    # Need to apply backpropogation for every data point, delta variables correspond to errors in activations. 
    for i in range(m):
        delta_3 = pred[i,:] - Y[i,:]
        z_2 = np.matmul(Theta_1, X[i,:])
        a_2 = sigmoid(z_2)
        a_2 = np.insert(a_2, 0, 1)
        delta_2 = np.multiply(np.matmul(Theta_2.T, delta_3), sigmoid_grad(np.insert(z_2,0,1,axis=0)))
        z_3 = np.matmul(Theta_2, a_2)
        a_3 = sigmoid(z_3)

        # Implementing the backprop to update the derivatives. 
        grad_1 += np.outer(delta_2[1:], X[i,:])
        grad_2 += np.outer(delta_3, a_2)

    grad_1 = 1/m * grad_1 
    grad_2 = 1/m * grad_2 

    # Add derivative of regularisation terms into gradients.
    Theta_1_copy = np.copy(Theta_1)
    Theta_2_copy = np.copy(Theta_2)

    Theta_1_copy[:,0] = 0
    Theta_2_copy[:,0] = 0
    grad_1 += lambd/m * Theta_1_copy
    grad_2 += lambd/m * Theta_2_copy 

    grad_1 = grad_1.reshape((1,hidden_layer*(input_layer+1)))
    grad_2 = grad_2.reshape((1, output_layer*(hidden_layer+1)))
    grad = np.hstack((grad_1,grad_2))
    grad = grad.flatten()

    return cost, grad 







