import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
seeds = pd.read_table('Datasets/wheat.data', delimiter = ',', index_col = 0)

#
# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features

s1 = seeds.loc[:, ['area', 'perimeter']]

# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features

s2 = seeds.loc[:, ['groove', 'asymmetry']]

#
# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
#
s1.plot.hist(alpha=0.75)
s2.plot.hist(alpha=0.75)

# Display the graphs:
plt.show()

