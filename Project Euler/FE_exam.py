import numpy as np

A = np.array([[1,1,1,1], [0,0,1,1],[0,1,0,1],[0,0,0,1]])



B = np.array([[0,1,0,-9],[0,0,1,-9],[1,-1,-1,-9],[0,0,0,27]])

print(np.linalg.inv(B))

