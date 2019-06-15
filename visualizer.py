#!/usr/bin/python3

import pandas as pd
from glob import glob

def concat():
    b=pd.read_csv('italysliced.csv')
    print(b.columns)
    for file in glob('*.csv'):
        print(file)
        if file != 'italy.csv':
            a=pd.read_csv(file)
            print(a.columns)
            b=b.append(a)
    return b
    
def clean(file):
    df=pd.read_csv(file)
    df1=df[["Date","Season","home","visitor","FT","hgoal","vgoal"]]
    df1.to_csv(file[0:len(file)-4]+'sliced.csv')

def get_names(df):
    names= df.home.unique()
    return names

def create_results(df):
    results=[]
    for index, row in df.iterrows():
        if row['hgoal'] > row['vgoal']:
            results.append('0')
        elif row['hgoal'] < row['vgoal']:
            results.append('2')
        else:
            results.append('1')
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

data=pd.read_csv('try.csv')
data=data.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1'],1)
data=data.dropna()
names=get_names(data)

def past_games(df):
    for index in range(df.shape[0]):
        name=df.at[index,'home']
        for ix in range(df.shape[0]):
            if df.at[ix,'home'] == name:
                print(df.loc[[ix]])

#print(past_games(data))

def change_date(df):
    new_dates=[]
    old_dates=list(df['Date'].values)
    for x in old_dates:
        day=x[8:10]
        month=x[5:7]
        year=x[0:4]
        new_date=day+'/'+month+'/'+year
        new_dates.append(new_date)
    return new_dates

data['Date']=change_date(data)

print(data.head())
