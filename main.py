#!/usr/bin/python3

import functions

from datetime import datetime
import pandas as pd
import numpy as np
from glob import glob

#data=pd.read_csv('somedata.csv')
data=pd.read_csv('usa_worked.csv')
data=data.drop(['Unnamed: 0'],1)

hgoaldiff_50=[]
hgoaldiff_5=[]
hfatigue=[]
hpoints_15=[]
hpoints_5=[]

vgoaldiff_50=[]
vgoaldiff_5=[]
vfatigue=[]
vpoints_15=[]
vpoints_5=[]

for ix in range(data.shape[0]):
    hrows=functions.past_games(data,data.loc[ix,'Date'],data.loc[ix,'home'],50)
    vrows=functions.past_games(data,data.loc[ix,'Date'],data.loc[ix,'visitor'],50)
    print(ix)
    
    hfatigue.append(functions.create_fatigue(hrows))
    hgoaldiff_50.append(functions.avg_goaldiff(hrows,50))
    hgoaldiff_5.append(functions.avg_goaldiff(hrows,5))
    hpoints_15.append(functions.get_points(hrows,50))
    hpoints_5.append(functions.get_points(hrows,5))

    vfatigue.append(functions.create_fatigue(vrows))
    vgoaldiff_50.append(functions.avg_goaldiff(vrows,50))
    vgoaldiff_5.append(functions.avg_goaldiff(vrows,5))
    vpoints_15.append(functions.get_points(vrows,50))
    vpoints_5.append(functions.get_points(vrows,5))

data['hfatigue']=hfatigue
data['havg_diff50']=hgoaldiff_50
data['havg_diff5']=hgoaldiff_5
data['havg_points15']=hpoints_15
data['havg_points5']=hpoints_5

data['vfatigue']=vfatigue
data['vavg_diff50']=vgoaldiff_50
data['vavg_diff5']=vgoaldiff_5
data['vavg_points15']=vpoints_15
data['vavg_points5']=vpoints_5

data.to_csv('final_usa.csv')

