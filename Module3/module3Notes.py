# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 21:42:36 2017

@author: Mark
"""
####################################################################################
####################################################################################
############################ MODULE 3 -- EXPLORING DATA ############################
####################################################################################
####################################################################################

import matplotlib as mp
import matplotlib.pyplot as plt
import pandas as pd

mp.style.use('ggplot')

### Section 1: Basic Plots ###

####################
#### Histograms ####
####################
students = pd.read_table('Datasets\students.data', delimiter=',', index_col=0)
students.head(5)

# make a histogram of one field
g3 = students.G3
g3.plot.hist(alpha=0.5)

# make a histogram of multiple fields
g321 = students[['G3', 'G2', 'G1']]
g321.plot.hist(alpha=0.5)

####################
## Scatter plots ###
####################

# basic 2-d scatter plot
students.plot.scatter(x = 'G1', y = 'G3')

# more advanced 3-d scatter]
from mpl_toolkits.mplot3d import Axes3D
# for these, we actually need to use matplotlib to create a plot object:
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Daily Alcohol')

ax.scatter(students.G1, students.G3, students.Dalc, c='r', marker='.')
plt.show()

### Section 2: Higer Dimensionality Visualizations ###

# parallel coordinates plot
from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates, andrews_curves

data = load_iris()
df = pd.DataFrame(data.data, columns = data.feature_names)

df['target_names'] = [data.target_names[i] for i in data.target]

plt.figure()
parallel_coordinates(df, 'target_names')
plt.show()

# andrews plot
plt.figure()
andrews_curves(df, 'target_names')
plt.show()

# imshow
import numpy as np

df = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
df.corr()

plt.figure()
plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)