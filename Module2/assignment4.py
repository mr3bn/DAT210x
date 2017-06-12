import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading

df = pd.read_html('http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2', header=1)[0]

# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#

n = ['Rank', 'Player', 'Team', 'GamesPlayed', 'Goals', 'Assists', 'Points', 'PlusMinus', 'PenaltyMinutes', 'PointsPerGame', 'ShotsOnGoal', 'ShootingPct', 'GameWinners', 'PowerPlayGoals', 'PowerPlayAssists', 'ShortHandGoals', 'ShortHandAssists']
df.columns = n

# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics

df = df[df.isnull().sum(axis=1) < 4]

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#

for i in range(0, len(df.columns)):
    c = df.iloc[:, i]
    if pd.isnull(pd.to_numeric(c[0], errors='coerce')):
        next
    else:
        c = pd.to_numeric(c, errors='coerce')
        df.iloc[:, i] = c
    
df = df[df.isnull().sum(axis=1) != 15]

# TODO: Get rid of the 'RK' column
del df['Rank']

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index

df.reset_index(drop=1)

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
#

for i in range(0, len(df.columns)):
    # print the column's name and datatype of its elements
    # each column should be atomic at this point, 
    # so we're just checking for proper type
    c = df.iloc[:, i]
    typeString = c.dtype.str
    print df.columns[i] + ': ' + typeString


# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#

# how many rows remain in the dataset?
print len(df)

# how many unique PCT values exist in the table?
print len(df.loc[:, 'ShootingPct'].unique())

# what's the value of adding games played at indeces 15 and 16?
# ...actually 14 and 15.....
print df.loc[14, 'GamesPlayed'] + df.loc[15, 'GamesPlayed']
