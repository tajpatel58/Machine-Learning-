import numpy as np 
from PIL import Image


def pixel_picture(file_path, pixel_dim):
    """
    This method is used to obtain a pixel picture and a feature vector that somewhat corresponds 
    with our MNIST data. I say somewhat as there needs to be some more pre-processing however I felt this was sufficient 
    for now. A pixel picture is a pixel_dim x pixel_dim matrix whose entries are between 0 and 1. They correspond to grayscale
    values. 

    Params: 
        file_path (string): A string file path for the jpeg which you want a pixel picture and feature vector for.
        pixel_dim (int): Number of columns/rows you want to divide the data to. This in general should be set to 20 for our
                         model. 
                        
    Returns: 
        pixel_image (numpy array): A pixel picture is a pixel_dim x pixel_dim matrix whose entries are between 0 and 1. 
                                   They correspond to grayscale values. 
        feature_vec (numpy array): A feature vector obtained from the pixel picture, can be used in our model. 
    
    """
    image = Image.open(file_path)
    grayscale_img = image.convert(mode='L')
    grayscale_img = grayscale_img.resize((pixel_dim,pixel_dim))
    pixel_image = np.invert(np.asarray(grayscale_img)).T
    feature_vec = pixel_image.reshape((1,pixel_dim*pixel_dim))/255
    feature_vec = np.insert(feature_vec, 0, 1, axis=1)
    return [pixel_image, feature_vec]