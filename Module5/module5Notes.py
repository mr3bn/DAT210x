# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:21:21 2017

@author: mrossi
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

data = [0,1,2,3,4,5,6,7,8,9]
labels=[0,0,0,0,0,1,1,1,1,1]

data_train, data_test, label_train, label_test = train_test_split(data, labels, test_size = 0.5, random_state=7)

print data_train
print label_train
print data_test
print label_test

X_train = pd.DataFrame([[0], [1], [2], [3]])
y_train = [0, 0, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

print model.predict([[1.1]])

print model.predict_proba([[0.9]])