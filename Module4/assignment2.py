import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import assignment2_helper as helper
from sklearn.decomposition import PCA

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


# Do * NOT * alter this line, until instructed!
scaleFeatures = True


# TODO: Load up the dataset and remove any and all
# Rows that have a nan. You should be a pro at this
# by now ;-)

kidney = pd.read_csv('Datasets/kidney_disease.csv', index_col=0)
kidney = kidney.dropna()
kidney = kidney.reset_index()

# QUESTION: Should the id column be included as a
# feature?
#

# no -- but added it as the index column so should be fine, right?


# Create some color coded labels; the actual label feature
# will be removed prior to executing PCA, since it's unsupervised.
# You're only labeling by color so you can see the effects of PCA
labels = ['blue' if i=='ckd' else 'orange' for i in kidney.classification]


# TODO: Use an indexer to select only the following columns:
#       ['bgr','wc','rc']
#

df = kidney.loc[:, ['bgr', 'wc', 'rc']]

# TODO: Print out and check your dataframe's dtypes. You'll might
# want to set a breakpoint after you print it out so you can stop the
# program's execution.
#
# You can either take a look at the dataset webpage in the attribute info
# section: https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease
# or you can actually peek through the dataframe by printing a few rows.
# What kind of data type should these three columns be? If Pandas didn't
# properly detect and convert them to that data type for you, then use
# an appropriate command to coerce these features into the right type.
#

for i in range(0, len(df.columns)):
    c = df.iloc[:, i]
    typeString = c.dtype.str
    print df.columns[i] + ': ' + typeString
    
# looks like wc and rc need coersion into int and float, respectively
df.loc[:, 'wc'] = pd.to_numeric(df.loc[:, 'wc'], errors='coerce')
df.loc[:, 'rc'] = pd.to_numeric(df.loc[:, 'rc'], errors='coerce')

# double-check...

for i in range(0, len(df.columns)):
    # so we're just checking for proper type
    c = df.iloc[:, i]
    typeString = c.dtype.str
    print df.columns[i] + ': ' + typeString
    
# ...looks good


# TODO: PCA Operates based on variance. The variable with the greatest
# variance will dominate. Go ahead and peek into your data using a
# command that will check the variance of every feature in your dataset.
# Print out the results. Also print out the results of running .describe
# on your dataset.
#
# Hint: If you don't see all three variables: 'bgr','wc' and 'rc', then
# you probably didn't complete the previous step properly.
#

print df.var()
print df.describe()


# TODO: This method assumes your dataframe is called df. If it isn't,
# make the appropriate changes. Don't alter the code in scaleFeatures()
# just yet though!
#
# .. your code adjustment here ..
if scaleFeatures: df = helper.scaleFeatures(df)


# TODO: Run PCA on your dataset and reduce it to 2 components
# Ensure your PCA instance is saved in a variable called 'pca',
# and that the results of your transformation are saved in 'T'.
#

pca = PCA(n_components = 2, svd_solver = 'full')
pca.fit(df)
  
PCA(copy=True, n_components=2, whiten=False)
T=pca.transform(df)
  
# Plot the transformed data as a scatter plot. Recall that transforming
# the data will result in a NumPy NDArray. You can either use MatPlotLib
# to graph it directly, or you can convert it to DataFrame and have pandas
# do it for you.
#
# Since we've already demonstrated how to plot directly with MatPlotLib in
# Module4/assignment1.py, this time we'll convert to a Pandas Dataframe.
#
# Since we transformed via PCA, we no longer have column names. We know we
# are in P.C. space, so we'll just define the coordinates accordingly:
    
ax = helper.drawVectors(T, pca.components_, df.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
T.columns = ['component1', 'component2']
T.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, ax=ax)
plt.show()
