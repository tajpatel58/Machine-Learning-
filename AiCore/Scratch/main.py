

#%%
 
import os 
import pandas as pd 


info_dict = {'Name':['Taj', 'Radhika'], 'Age': [23, 24]}

a = pd.DataFrame(info_dict)
a.to_csv(f'{os.getcwd()}/test_folder/hello.csv')
print(str(os.getcwd())+'/Hello')


# %%
