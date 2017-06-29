import matplotlib.pyplot as plt

import pandas as pd


def load(path_test, path_train):
  # Load up the data.
  # You probably could have written this..
  with open(path_test, 'r')  as f: testing  = pd.read_csv(f)
  with open(path_train, 'r') as f: training = pd.read_csv(f)

  # The number of samples between training and testing can vary
  # But the number of features better remain the same!
  n_features = testing.shape[1]

  X_test  = testing.ix[:,:n_features-1]
  X_train = training.ix[:,:n_features-1]
  y_test  = testing.ix[:,n_features-1:].values.ravel()
  y_train = training.ix[:,n_features-1:].values.ravel()

  #
  # Special:

  return X_train, X_test, y_train, y_test


def peekData(x):
  # The 'targets' or labels are stored in y. The 'samples' or data is stored in X
  print "Peeking your data..."
  fig = plt.figure()

  cnt = 0
  for col in range(5):
    for row in range(10):
      plt.subplot(5, 10, cnt + 1)
      plt.imshow(x.ix[cnt,:].reshape(8,8), cmap=plt.cm.gray_r, interpolation='nearest')
      plt.axis('off')
      cnt += 1
  fig.set_tight_layout(True)
  plt.show()


def drawPredictions(model, X_train, X_test, y_train, y_test):
  fig = plt.figure()

  # Make some guesses
  y_guess = model.predict(X_test)


  #
  # INFO: This is the second lab we're demonstrating how to
  # do multi-plots using matplot lab. In the next assignment(s),
  # it'll be your responsibility to use this and assignment #1
  # as tutorials to add in the plotting code yourself!
  num_rows = 10
  num_cols = 5

  index = 0
  for col in range(num_cols):
    for row in range(num_rows):
      plt.subplot(num_cols, num_rows, index + 1)

      # 8x8 is the size of the image, 64 pixels
      plt.imshow(X_test.ix[index,:].reshape(8,8), cmap=plt.cm.gray_r, interpolation='nearest')

      # Green = Guessed right
      # Red = Fail!
      fontcolor = 'g' if y_test[index] == y_guess[index] else 'r'
      plt.title('Label: %i' % y_guess[index], fontsize=6, color=fontcolor)
      plt.axis('off')
      index += 1
  fig.set_tight_layout(True)
  plt.show()
  
X = pd.read_table('Datasets/parkinsons.data', delimiter=',', index_col='name')
y = X['status']
del X['status']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 7)

import sklearn.preprocessing as pre

transformer = pre.StandardScaler()
transformer.fit(X_train)

X_train = transformer.transform(X_train)
X_test = transformer.transform(X_test)

#from sklearn.decomposition import PCA
#pca = PCA(n_components=14)
#pca.fit(X_train)
#X_train = pca.transform(X_train)
#X_test = pca.transform(X_test)

from sklearn import manifold
iso = manifold.Isomap(n_neighbors=5, n_components=6)
iso.fit(X_train)
X_train = iso.transform(X_train)
X_test = iso.transform(X_test)

from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train, y_train)

print svc.score(X_test, y_test)

import numpy as np
c_range = np.arange(0.05, 2, 0.05)
gamma_range = np.arange(0.001, 0.1, 0.001)

best_c = 0
best_gamma = 0
best_score = 0

for c in c_range:
    for g in gamma_range:
        svc = SVC(C=c, gamma=g)
        svc.fit(X_train, y_train)
        if svc.score(X_test, y_test) > best_score:
            best_c = c
            best_gamma = g
            best_score = svc.score(X_test, y_test)

print best_score
print 'C: ', best_c
print 'gamma: ', best_gamma
