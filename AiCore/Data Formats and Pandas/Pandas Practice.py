#%%
import pandas as pd
from pprint import pprint 

# User information dictionary, in JSON format. 
a = [{'Name':'Taj', 'Age': 23, 'Birth Month': 'August', 'Degree': 'Mathematics'},
     {'Name': 'Radhika', 'Age' : 24, 'Birth Month' : 'September'}]

# Convert to dataframe:
df = pd.json_normalize(a)

pprint(df)

# %%
# Import Pokemon dataset.

poke = pd.read_csv('pokemon_data.csv')

# Get the headers of our dataframe. 
headers = poke.columns

# New df for names and types. 
poke_names_and_Type_1 = poke[['Name', 'Type 1']]

# New df for the first 5 pokemon in dataset. 
first_5_poke = poke.iloc[0:5]

# Dataframe for fire pokemon. 
fire_poke = poke.loc[poke['Type 1'] == 'Fire']

# Highest health sorted df:
HP_poke = poke.sort_values('HP', ascending=0)

# Pikachu information:
pikachu = poke.loc[poke['Name'] == 'Pikachu']

# Lets add a total for the speed,health, etc as some measure of overall
# performance. 
poke['Total'] = poke.iloc[:, 4:10].sum(axis=1)

# Lets store top 10 pokem=on
top_10_poke = poke.sort_values('Total', ascending=0).head(10)

# Let's add total after types to reoganise our data. 
cols = list(poke.columns.values)
cols.insert(4, 'Total')
new_cols = cols[:-2]

# Reorganised Data: 
poke = poke[new_cols]
# %%
# In this cell I try to deeper into how we can filter data. 

# Suppose we want to set multiple filters in loc, we want Fire and Electric pokemon:

f_and_e_poke = poke.loc[(poke['Type 1'] == 'Fire') | (poke['Type 1'] == 'Electric')]

# Lets try filter for these pokemon that have attack > 80

attack_more_than_eighty = f_and_e_poke.loc[f_and_e_poke['Attack'] > 80]

# Suppose we want to remove all the pokemon with the "mega" in their names:

no_mega_poke = poke.loc[~poke['Name'].str.contains('Mega')]

# Lets introudce the idea that a pokemon is 'Good' if their total is > 600
poke['Good'] = 0

# Remark, we can also replace 'Good' with multiple column names and this would change 
# multiple columns. 
poke.loc[poke['Total'] > 600, 'Good'] = 1 


# %%
# Aggregate Statistics (GroupBy):

# Note statistical operations only work for numerical data, hence
# the other columns are ommitted. 

# Suppose we want to group by the 'Good' pokemon and see how the
# statistics for HP/Attack etc vary. 

mean_good_groupby = poke.groupby(['Good']).mean()

# Suppose now we want to see the mean statistics based upon the pokemon 
# Type 1 and we only want this data for Total/HP/Attack/Defense, to do this
# we can pass a boolean list describing which columns we want. 

type_groupby = poke.groupby(['Type 1']).mean().iloc[:, 1:5]

# Now suppose we want to sort this new dataframe by total, this would
# be to see the "best" type 1 category for pokemon.

sorted_type_1 = type_groupby.sort_values('Total', ascending=False)

# After printing this table we can see Dragon, Steel types are the "best"
# whereas Bug and Poison tend to be the worst. 

# Lets obtain the counter for each category in Type 1

counter_type_1 = poke.groupby(['Type 1']).count().iloc[:, 0]

print(counter_type_1)
# %%
