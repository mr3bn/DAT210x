import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#

n = ['motor', 'screw', 'pgain', 'vgain', 'class']

df = pd.read_table('Datasets/servo.data', delimiter=',', names=n)

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#

df_adj = df[df.vgain == 5]
print df_adj.shape[0]

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#

df_adj2 = df[(df.motor == 'E') & (df.screw == 'E')]
print df_adj2.shape[0]


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#

df_adj3 = df[df.pgain == 4]
print sum(df_adj3.loc[:, 'vgain'])  / df_adj3.shape[0]


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!

print df.dtypes

