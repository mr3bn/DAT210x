import pandas as pd


#https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names


# 
# TODO: Load up the mushroom dataset into dataframe 'X'
# Verify you did it properly.
# Indices shouldn't be doubled.
# Header information is on the dataset's website at the UCI ML Repo
# Check NA Encoding
#

X = pd.read_table('Datasets/agaricus-lepiota.data', index_col=None, header=0, delimiter=',')

headers = ['label', 'cap_shape', 'cap_surface', 'cap_color', 'bruises', 'odor', 
           'gill_attachment', 'gill_spacing', 'gill_size', 'gill_color', 
           'stalk_shape', 'stalk_root', 'stalk_surface_above', 
           'stalk_surface_below', 'stalk_color_above', 'stalk_color_below',
           'veil_type', 'veil_color', 'ring_number', 'ring_type', 'spore_print', 
           'population', 'habitat']
X.columns = headers

# INFO: An easy way to show which rows have nans in them
#print X[pd.isnull(X).any(axis=1)]


# 
# TODO: Go ahead and drop any row with a nan
#
df = X.dropna()

print X.shape


#
# TODO: Copy the labels out of the dset into variable 'y' then Remove
# them from X. Encode the labels, using the .map() trick we showed
# you in Module 5 -- canadian:0, kama:1, and rosa:2
#

y = X['label'].map({'p' : 0, 'e' : 1})
del X['label']

#
# TODO: Encode the entire dataset using dummies
#
X = pd.get_dummies(X, prefix=X.columns)


# 
# TODO: Split your data into test / train sets
# Your test size can be 30% with random_state 7
# Use variable names: X_train, X_test, y_train, y_test
#
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 7)


#
# TODO: Create a DT classifier. No need to set any parameters
#
from sklearn import tree
dt = tree.DecisionTreeClassifier()
 
#
# TODO: train the classifier on the training data / labels:
# TODO: score the classifier on the testing data / labels:
#
dt.fit(X_train, y_train)
score = dt.score(X_test, y_test)


print "High-Dimensionality Score: ", round((score*100), 3)

print dt.feature_importances_

#
# TODO: Use the code on the course's SciKit-Learn page to output a .DOT file
# Then render the .DOT to .PNGs. Ensure you have graphviz installed.
# If not, `brew install graphviz`. If you can't, use: http://webgraphviz.com/.
# On Windows 10, graphviz installs via a msi installer that you can download from
# the graphviz website. Also, a graph editor, gvedit.exe can be used to view the
# tree directly from the exported tree.dot file without having to issue a call.
#

d = tree.export_graphviz(dt, out_file='pic.dot')