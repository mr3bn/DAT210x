# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 14:30:05 2017

@author: Mark
"""

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

# some import examples
#df = pd.read_sql_table('my_table', engine, columns = ['ColA', 'ColB'])
#df = pd.read_excel('my_dataset.xlsx', 'Sheet1', na_values=['NA'])
#df = pd.read_json('my_dataset.json', orient='columns')
#df = pd.read_csv('my_dataset.csv')
#
## writing is easy, too
#df.to_sql('table', engine)
#df.to_excel('dataset.xlsx')
#df.to_json('dataset.json')
#df.to_csv('dataset.csv')

# none of those will work, so let's do one that will:
    
df = pd.read_csv('Datasets/direct_marketing.csv')

# basic summary stuff included in pandas...
print df.head(5)
print df.tail(5)
print df.describe()
print df.columns

#################### COLUMN INDEXING ####################

# one way to get a single column out of data frame is to access it by name...
# this syntax will return a SERIES object of one column, size=nrow:
rec = df.recency
rec = df['recency']

# doubling up on the brackets returns a DATA FRAME of the same column, size=nrowx1
# intuitively, the interior set of brackets is a list in itself, 
# so this application can actually handle more than one column:
rec = df[['recency']]
rec = df[['recency', 'history']]

# the df.loc method provides a marginally faster way to access a column by name...
# same series of size=nrow, just using a different method:
rec = df.loc[:, 'recency']

# and this application will again return a data frame (nrowx1)
rec = df.loc[:, ['recency']]
# same story, can slice to > 1 column:
rec = df.loc[:, ['recency', 'history']]

# df.loc also works with boolean masks, but won't bother with that right now

# the df.iloc method uses numbered indexes instead of names
rec = df.iloc[:, 0]
rec = df.iloc[:, [0]]

# IMPORTANT: for the list implementation of .iloc, note that the results
# are NOT inclusive. 
rec = df.iloc[:, 0:1] # returns the same as df.iloc[:, [0]]

# df.ix is sort of a hybrid of .loc and .iloc
rec = df.ix[:, 0]
rec = df.ix[:, 'recency']
rec = df.ix[:, 0:1]

#################### ROW INDEXING ####################

# one easy way to subest rows is with a boolean operation...

df.recency < 7 # returns a series of booleans, which we can use as a mask:
df[df.recency < 7]

# this methodology can work with multiple boolean tests:
df[(df.recency < 7) & (df.newbie == 0)]

# it's also possible to write to a dataframe into a slice:
# df[df.recency < 7] = -100 will render ALL rows in the data frame as -100
# where recency is < 7. a better implementation is to do this for one 
# column at a time, to account for data frame nonhomogeneity