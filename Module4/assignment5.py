import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import os
import random, math

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')

def Plot2D(T, col, title, x, y, num_to_plot=40):
  # This method picks a bunch of random samples (images in your case)
  # to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  ax.scatter(T[:,x], T[:,y], marker='.', alpha=0.7, c=col)
  

def Plot3D(T, title, x, y, z, number_to_plot=40):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(title)
    ax.set_xlabel('Component: {0}'.format(x))
    ax.set_ylabel('Component: {0}'.format(y))
    ax.set_zlabel('Component: {0}'.format(z))
    ax.scatter(T[:, x], T[:, y], T[:, z], marker='.', alpha=0.7)
    
#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
samples = []
colors = []
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.

# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#

dir32 = os.getcwd() + '/Datasets/ALOI/32'

for f in os.listdir(dir32):
    img = misc.imread(dir32 + '/' + f)
    X = (img / 255.0).reshape(-1)
    samples.append(X)
    colors.append('b')
    
df = pd.DataFrame(samples)

from sklearn import manifold
iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO, k=6", 0, 1)

iso = manifold.Isomap(n_neighbors=5, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO: k=5", 0, 1)

iso = manifold.Isomap(n_neighbors=4, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO, k=4", 0, 1)

iso = manifold.Isomap(n_neighbors=3, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO, k=3", 0, 1)

iso = manifold.Isomap(n_neighbors=2, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO, k=2", 0, 1)

iso = manifold.Isomap(n_neighbors=1, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO, k=1", 0, 1)

#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#

dir32i = os.getcwd() + '/Datasets/ALOI/32i'

for f in os.listdir(dir32i):
    img = misc.imread(dir32i + '/' + f)
    X = (img / 255.0).reshape(-1)
    samples.append(X)
    colors.append('r')
    
#
# TODO: Convert the list to a dataframe
#
df = pd.DataFrame(samples)

iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO, k=6, both dirs", 0, 1)

iso = manifold.Isomap(n_neighbors=5, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO: k=5, both dirs", 0, 1)

iso = manifold.Isomap(n_neighbors=4, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO, k=4, both dirs", 0, 1)

iso = manifold.Isomap(n_neighbors=3, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO, k=3, both dirs", 0, 1)

iso = manifold.Isomap(n_neighbors=2, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO, k=2, both dirs", 0, 1)

iso = manifold.Isomap(n_neighbors=1, n_components=3)
iso.fit(df)
T = iso.transform(df)
Plot2D(T, colors, "3d ISO, k=1", 0, 1)

#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 



#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 




#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 



plt.show()

