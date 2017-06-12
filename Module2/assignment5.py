import pandas as pd
import numpy as np


#
# TODO:
# Load up the dataset, setting correct header labels.
#

census = pd.read_table('Datasets/census.data', delimiter=',', header=None, index_col=0)

n = ['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification']
census.columns = n

#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#

print census.head(5)
    
# some ? values in the capital-gain column...

pd.to_numeric(census.loc[:, 'capital-gain'], errors='coerce')

#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). If you ever get confused, think to yourself
# what makes more sense generally---to represent such features with a
# continuous numeric type... or a series of categories?
#
for i in range(0, len(census.columns)):
    # print the column's name and datatype of its elements
    # each column should be atomic at this point, 
    # so we're just checking for proper type
    c = census.iloc[:, i]
    typeString = c.dtype.str
    print census.columns[i] + ': ' + typeString
    
# encode the education field (ordinal)
    
ordered_education = ['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th', '12th', 'HS-grad', 'Some-college', 'Bachelors', 'Masters', 'Doctorate']
census.education = census.education.astype('category', ordered=True, categories=ordered_education).cat.codes

# encode the classification field (ordinal)

ordered_classification = ['<=50K', '>50K']
census.classification = census.classification.astype('category', ordered=True, categories=ordered_classification).cat.codes

# encode the race and sex fields (nominal)
census = pd.get_dummies(census, columns=['race', 'sex'])

#
# TODO:
# Print out your dataframe
#
# .. your code here ..


