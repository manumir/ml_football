#!/usr/bin/python3

import functions

from datetime import datetime
import pandas as pd
from glob import glob

data=pd.read_csv('somedata.csv')
data=data.drop(['Unnamed: 0'],1)

rows=functions.past_games(data,'1929-12-13',data.loc[100,'home'])
rows=rows.reset_index()
print(rows[-1:])
print(functions.points(rows))

print(functions.create_fatigue(rows))
print(functions.avg_goaldiff(rows))

print(data.head())

