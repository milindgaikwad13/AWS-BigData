import numpy as np
import pandas as pd


lables = ['a','b','c']
my_data = [10,20,30]


arr = np.array(my_data)
d={'a':10, 'b':20, 'c':30}

print(arr)


pd_series= pd.Series(data = my_data, index= lables)
pd_series= pd.Series(my_data,lables)

print(pd_series)

pd_series= pd.Series(d)

print(pd_series)


pd_series= pd.Series(arr)

print(pd_series)