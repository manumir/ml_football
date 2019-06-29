#!/usr/bin/python3

import functions

from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

data=pd.read_csv('somedata.csv')
data=data.drop(['Unnamed: 0'],1)

rows=functions.past_games(data,'3999-12-13','NK Zagreb',10)
rows=rows.reset_index()
rows.pop('index')
print(rows)

print(functions.create_fatigue(rows))
print(functions.avg_goaldiff(rows))

data=data.reset_index(drop=True)

a,b=functions.get_tiers(data)
ixes=[]
for ix in range(data.shape[0]):
    for name in a:
        if data.loc[ix,'home']==name:
            ixes.append(ix)
print(ixes)

for ix in ixes:
    data=data.drop(ix)
    
data=data.reset_index(drop=True)
data.to_csv('a.csv')
a,b=functions.get_tiers(data)
plt.plot(b)
plt.show()


'''for ix in range(data.shape[0]):
    rows=functions.past_games(data,data.loc[ix,'Date'],data.loc[ix,'home'],10)
    print(rows,ix)'''
