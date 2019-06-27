#!/usr/bin/python3

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
            results.append('0')
        else:
            results.append('-1')
    return results 

def winrates(data):
    home,away,draw=0,0,0
    for value in data['result'].values:
        if value == 0:
            home+=1
        elif value == 1:
            draw+=1
        else:
            away+=1
    print('home :{}%\naway :{}%\ndraw :{}%\n'.format((home/data.shape[0])*100,
        (away/data.shape[0])*100,(draw/data.shape[0])*100))

def past_games(df,data1,team):
    pgames=[]
    name=team
    data1=data1
    rows=df.loc[df['home'] == 'Real Madrid']
    return rows.loc[rows['Date'] < data1]

def create_goaldiff(df):
    diff=[]
    for index in range(data.shape[0]):
        diff.append(data.loc[index,'hgoal'] - data.loc[index,'vgoal'])
    return diff

def create_fatigue(df):
    from datetime import datetime
    date_format = "%Y-%m-%d"
    days=[]
    for ix in range(data.shape[0]):
        a = datetime.strptime(df.loc[ix,'Date'], date_format)
        b = datetime.strptime(df.loc[ix+1,'Date'], date_format)
        days.append(b-a)
    return days

data=pd.read_csv('somedata.csv')
data=data.drop(['Unnamed: 0'],1)

print(past_games(data,'1929-06-13',data.loc[100,'home']))

print(data.head())


