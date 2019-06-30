#!/usr/bin/python3

import functions

from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

data=pd.read_csv('somedata.csv')
data=data.drop(['Unnamed: 0'],1)
final=data

for ix in range(data.shape[0]):
    goaldiff=[]
    fatigue=[]
    points=[]
    delete=[]

    rows=functions.past_games(data,data.loc[ix,'Date'],data.loc[ix,'home'],30)
    print(ix,final.shape[0])
    if rows.empty:
        final=final.drop(ix)
        final=final.reset_index(drop=True)
        print('empty df')

    fatigue.append(functions.create_fatigue(rows))
    goaldiff.append(functions.avg_goaldiff(rows))
    points.append(functions.get_points(rows,15))

final['fatigue']=fatigue
final['avg_diff30']=goaldiff
final['avg_points15']=points

final.to_csv('final.csv')
