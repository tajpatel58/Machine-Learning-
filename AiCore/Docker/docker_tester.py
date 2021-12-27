import pandas as pd 
import numpy as np

data = np.array([[1,2],[3,4]])

df = pd.DataFrame(data, columns=['Odd', 'Even'])

print(df)