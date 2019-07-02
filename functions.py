#!/usr/bin/python3

from datetime import datetime
import pandas as pd
import numpy as np
from glob import glob

def concat():
    b=pd.read_csv('scotland.csv')
    for file in glob('*.csv'):
        print(file)
        if file != 'scotland.csv':
            a=pd.read_csv(file)
            b=b.append(a)
    return b

def clean(file):
    df=pd.read_csv(file)
    df1=df[["Date","home","visitor","hgoal","vgoal"]]
    df1.to_csv(file[0:len(file)-4]+'sliced.csv')
    return df1

def get_names(df):
    names= df.home.unique()
    return names

def create_results(df):
    results=[]
    for ix in range(df.shape[0]):
        if df.loc[ix,'hgoal'] > df.loc[ix,'vgoal']:
            results.append('1')
        elif df.loc[ix,'hgoal'] < df.loc[ix,'vgoal']:
            results.append('-1')
        else:
            results.append('0')
    return results 

def winrates(data):
    home,away,draw=0,0,0
    for value in data['result'].values:
        if value == 1:
            home+=1
        elif value == 0:
            draw+=1
        else:
            away+=1
    return home/data.shape[0]
    #print('home :{}%\naway :{}%\ndraw :{}%\n'.format((home/data.shape[0])*100,
     #   (away/data.shape[0])*100,(draw/data.shape[0])*100))

def past_games(df,data1,team,amount):
    pgames=[]
    name=team
    data1=data1
    rows=df.loc[df['home'] == team]
    rows=rows.loc[rows['Date'] < data1]
    return rows[-(amount):]

def create_goaldiff(df):
    diff=[]
    for index in range(df.shape[0]):
        diff.append(df.loc[index,'hgoal'] - df.loc[index,'vgoal'])
    return diff

def sub_dates(date1,date2):
    day1=int(date1[0:2])
    day2=int(date2[0:2])
    month1=int(date1[3:5])
    month2=int(date2[3:5])
    year1=int(date1[6:10])
    year2=int(date2[6:10])

    diff=(year1-year2)*365 + (month1-month2)*30 + (day1-day2)
    return diff

def sub_dates1(date1,date2):
    year1=int(date1[0:4])
    year2=int(date2[0:4])
    month1=int(date1[5:7])
    month2=int(date2[5:7])
    day1=int(date1[8:10])
    day2=int(date2[8:10])

    diff=(year1-year2)*365 + (month1-month2)*30 + (day1-day2)
    return diff

def create_fatigue(df):
    df=df.reset_index(drop=True)
#    date_format = "%Y-%m-%d"
    date_format = "%d/%m/%Y"
    try:
        a =df.loc[len(df)-2,'Date']
        b =df.loc[len(df)-1,'Date']
        days=sub_dates(b,a)
    except:
        days=np.nan
    return days

def avg_goaldiff(df,number_of_games):
    df=df[-(number_of_games):]
    df=df.reset_index(drop=True)

    count=0
    try:
        for value in df['goaldiff'].values:
            count+=value
        return count/(len(df['goaldiff'].values))
    except:
        return np.nan

def get_points(df,number_of_games):
    df=df[-(number_of_games):]
    df=df.reset_index()
    df.pop('index')
    
    points=0
    try:
        for ix in range(df.shape[0]):
            points+=df.loc[ix,'result']
        return points/df.shape[0]
    except:
        return np.nan

def get_tiers(df): #this need some work because not every league
                   #is on the same level
    names=get_names(df)
    points=[]
    for team in names:
        games=past_games(df,'2019-07-01',team,1000)
        a=get_points(games,1000)
        points.append(a)
    return points 


