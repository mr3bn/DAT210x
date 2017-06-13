import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
seeds = pd.read_table('Datasets/wheat.data', delimiter=',', index_col=0)



#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('Area')
ax.set_ylabel('Perimeter')
ax.set_zlabel('Asysmmetry')

ax.scatter(seeds.area, seeds.perimeter, seeds.asymmetry, c='r', marker='.')
plt.show()

#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('Width')
ax.set_ylabel('Groove')
ax.set_zlabel('Length')

ax.scatter(seeds.width, seeds.groove, seeds.length, c='green', marker='.')
plt.show()


