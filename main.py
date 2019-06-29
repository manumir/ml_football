#!/usr/bin/python3

import functions

from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

data=pd.read_csv('somedata.csv')
data=data.drop(['Unnamed: 0'],1)


#for ix in range(data.shape[0]):

rows=functions.past_games(data,data.loc[100,'Date'],data.loc[100,'home'],10)
print(rows)
print(functions.create_fatigue(rows))
    #print(functions.avg_goaldiff(rows))
    #print(rows,ix)
