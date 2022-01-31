#%%
# Here the taks will be to gain some familiarity with MatPlotLib,
# the data will be simply given as age of developers and their salaries. 

from matplotlib import pyplot as plt 

plt.style.use('seaborn-white')

plt.figure(dpi=1000)

# Median Developer Salaries by Age
ages = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


plt.plot(ages, dev_y, color='m',marker='o', label='All Devs')
plt.title('Developer Saries based on Age')
plt.xlabel('Age')
plt.ylabel('Salary($)')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages, py_dev_y, color='r',marker='x', label='Python Devs')

# Lets add some Javascript salaries:

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages, js_dev_y, color='b', marker='.', label='JavaScript Devs')

# Need to show our Legend:

plt.legend()

plt.savefig('Developer Salaries by Language.png')

plt.show()
# %%
