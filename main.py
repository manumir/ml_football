#!/usr/bin/python3

import functions

from datetime import datetime
import pandas as pd
import numpy as np
from glob import glob

data=pd.read_csv('somedata.csv')
data=data.drop(['Unnamed: 0'],1)

for ix in range(data.shape[0]):
    goaldiff=[]
    fatigue=[]
    points=[]

    rows=functions.past_games(data,data.loc[ix,'Date'],data.loc[ix,'home'],30)
    print(ix,final.shape[0])
    
    fatigue.append(functions.create_fatigue(rows))
    goaldiff.append(functions.avg_goaldiff(rows))
    points.append(functions.get_points(rows,15))

data['fatigue']=fatigue
data['avg_diff30']=goaldiff
data['avg_points15']=points

data.to_csv('final.csv')
