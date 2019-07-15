
import numpy as np
import pandas as pd
from numpy.random import randn



np.random.seed(101)


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

print(df)

print(df['W']) # this is a series


print(df[['W','Z']])


df['new'] = df['W'] + df['Z']
print(df)


df_new= df.drop('new',axis=1) # always creates new DF.. cant delete from current df

print(df_new)


df.drop('new',axis=1,inplace=True)
print(df)


print(df.loc['A'])


print(df.iloc[0])


print(df.loc['A',['Y']])

print(df>0)
