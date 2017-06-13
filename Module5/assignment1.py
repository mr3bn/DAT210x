#
# TODO: Import whatever needs to be imported to make this work
#
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Look Pretty
# matplotlib.style.use('ggplot')
#plt.style.use('ggplot')


#
# TODO: To procure the dataset, follow these steps:
# 1. Navigate to: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
# 2. In the 'Primary Type' column, click on the 'Menu' button next to the info button,
#    and select 'Filter This Column'. It might take a second for the filter option to
#    show up, since it has to load the entire list first.
# 3. Scroll down to 'GAMBLING'
# 4. Click the light blue 'Export' button next to the 'Filter' button, and select 'Download As CSV'


df = pd.read_csv('Datasets/crimes.csv', delimiter=',', header=0, index_col=0)

def doKMeans(df, k):
  #
  # INFO: Plot your data with a '.' marker, with 0.3 alpha at the Longitude,
  # and Latitude locations in your dataset. Longitude = x, Latitude = y
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.scatter(df.Longitude, df.Latitude, marker='.', alpha=0.3)

  #
  # TODO: Filter df so that you're only looking at Longitude and Latitude,
  # since the remaining columns aren't really applicable for this purpose.
  #
  
  df = df.loc[:, ['Longitude', 'Latitude']].dropna()
  
  #
  # TODO: Use K-Means to try and find seven cluster centers in this df.
  # Be sure to name your kmeans model `model` so that the printing works.
  #
  kmeans = KMeans(n_clusters=k)
  model = kmeans.fit(df)

  #
  # INFO: Print and plot the centroids...
  centroids = model.cluster_centers_
  ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
  return centroids



#
# TODO: Load your dataset after importing Pandas
#

df = pd.read_csv('Datasets/crimes.csv', delimiter=',', header=0, index_col=0)

#
# TODO: Drop any ROWs with nans in them
#
df = df.dropna()

#
# TODO: Print out the dtypes of your dset
#

for i in range(0, len(df.columns)):
    c = df.iloc[:, i]
    t = c.dtype.str

#
# Coerce the 'Date' feature (which is currently a string object) into real date,
# and confirm by re-printing the dtypes. NOTE: This is a slow process...
#
dCol = df.loc[:, 'Date']
df.loc[:, 'Date'] =  pd.to_datetime(dCol, errors='coerce')
df = df.dropna()


# INFO: Print & Plot your data
doKMeans(df)

#
# TODO: Filter out the data so that it only contains samples that have
# a Date > '2011-01-01', using indexing. Then, in a new figure, plot the
# crime incidents, as well as a new K-Means run's centroids.
#

df = df[df.loc[:,'Date'] > '2011-01-01']

# INFO: Print & Plot your data
doKMeans(df)
plt.show()