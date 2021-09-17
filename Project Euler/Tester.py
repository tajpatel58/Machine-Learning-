import numpy as np

A = np.array([[1,2],[3,4]])

B = np.array([5,6])

C = np.array([2,3])

print(np.einsum('ij,i,i->',A,B,C))