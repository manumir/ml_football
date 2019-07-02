#!/usr/bin/python3

import functions

from datetime import datetime
import pandas as pd
import numpy as np
from glob import glob

data=pd.read_csv('somedata.csv')
data=data.drop(['Unnamed: 0'],1)

goaldiff_50=[]
goaldiff_5=[]
fatigue=[]
points_15=[]
points_5=[]

for ix in range(data.shape[0]):
    rows=functions.past_games(data,data.loc[ix,'Date'],data.loc[ix,'home'],50)
    print(ix)
    
    fatigue.append(functions.create_fatigue(rows))
    goaldiff_50.append(functions.avg_goaldiff(rows,50))
    goaldiff_5.append(functions.avg_goaldiff(rows,5))
    points_15.append(functions.get_points(rows,15))
    points_5.append(functions.get_points(rows,5))

data['fatigue']=fatigue
data['avg_diff50']=goaldiff_50
data['avg_diff5']=goaldiff_5
data['avg_points15']=points_15
data['avg_points5']=points_5

data.to_csv('final.csv')

