#! /usr/bin/python3

import pandas as pd

data=pd.read_csv('final.csv')
data.pop('Unnamed: 0')

data=data.dropna()

data=data.drop(['Date','Season','hgoal','vgoal'],1)
print(data.head())

print(data.corr())

