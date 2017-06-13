import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
#

seeds = pd.read_table('Datasets/wheat.data', index_col=None, delimiter=',')



#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# 
del seeds['id']

#
# TODO: Compute the correlation matrix of your dataframe
# 
seeds.corr()


#
# TODO: Graph the correlation matrix using imshow or matshow
# 
plt.figure()
plt.imshow(seeds.corr(), interpolation='nearest')
plt.colorbar()
plt.show()


