#!/usr/bin/python3

from datetime import datetime
import pandas as pd
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
    df1=df[["Date","Season","home","visitor","FT","hgoal","vgoal"]]
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

def past_games(df,data1,team):
    pgames=[]
    name=team
    data1=data1
    rows=df.loc[df['home'] == 'Real Madrid']
    rows=rows.loc[rows['Date'] < data1]
    return rows

def create_goaldiff(df):
    diff=[]
    for index in range(df.shape[0]):
        diff.append(data.loc[index,'hgoal'] - data.loc[index,'vgoal'])
    return diff

def sub_dates(date1,date2):
    year1=int(date1[0:4])
    year2=int(date2[0:4])
    month1=int(date1[5:7])
    month2=int(date2[5:7])
    day1=int(date1[8:10])
    day2=int(date2[8:10])

    diff=(year1-year2)*365 + (month1-month2)*30 + (day1-day2)
    return diff

def create_fatigue(df):
    date_format = "%Y-%m-%d"
    days=[]
    for ix in range(df.shape[0]):
        try:
            a =df.loc[ix,'Date']
            b =df.loc[ix+1,'Date']
            days.append(sub_dates(b,a))
        except KeyError:
            days.append(-1)
    return days

def avg_goaldiff(df):
    count=0
    for value in df['goaldiff'].values:
        count+=value
    return count/(len(df['goaldiff'].values))

def points(df):
    df=df.reset_index()
    df.pop('index')
    
    points=0
    for ix in range(df.shape[0]):
        points+=df.loc[ix,'result']
    return points/df.shape[0]

