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
data=data.reset_index()
data.pop('index')
names=get_names(data)

def past_games(df,data1,team):
    pgames=[]
    name=team
    data1=data1
    rows=df.loc[df['home'] == 'Real Madrid']
    for value in rows['Date'].values:
        if value < data1:
            pgames.append(rows.loc[rows['Date']==value]) 
    return pgames

print(data.loc[131623:140664])
#data=data.reset_index()
#for index in range(data.shape[0]):
#    print(index,data.at[index,'hgoal'])

def create_result(df):
    result=[]
    for index in range(data.shape[0]):
        if data.loc[index,'hgoal'] > data.loc[index,'vgoal']:
            result.append(0)
        elif data.loc[index,'hgoal'] < data.loc[index,'vgoal']:
            result.append(1)
        else: 
            result.append(2)
    return result

data['result']=create_result(data)

print(data.head())

