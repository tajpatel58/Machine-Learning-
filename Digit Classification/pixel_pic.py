import numpy as np 
from PIL import Image


def pixel_picture(file_name, pixel_dim):
    image = Image.open(file_name)
    grayscale_img = image.convert(mode='L')
    grayscale_img = grayscale_img.resize((pixel_dim,pixel_dim))
    pixel_image = np.invert(np.asarray(grayscale_img)).T
    feature_vec = pixel_image.reshape((1,pixel_dim*pixel_dim))/255
    feature_vec = np.insert(feature_vec, 0, 1, axis=1)
    return [pixel_image, feature_vec]