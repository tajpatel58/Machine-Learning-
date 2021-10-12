
#%%
import yaml
import pandas as pd
from pprint import pprint 

with open('test.yml', "r") as stream:
    yaml_file = yaml.safe_load(stream)

print(yaml_file.values())
dataframe = pd.json_normalize(yaml_file.values())
pprint(dataframe)

# %%
