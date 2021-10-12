#%%
import pandas as pd
from pprint import pprint 

# User information dictionary.
a = [{'Name':'Taj', 'Age': 23, 'Birth Month': 'August', 'Degree': 'Mathematics'},
     {'Name': 'Radhika', 'Age' : 24, 'Birth Month' : 'September'}]

# Convert to dataframe:
df = pd.json_normalize(a)

pprint(df)

# %%
