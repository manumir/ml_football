#! /usr/bin/python3

import functions as f
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.svm import NuSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv('final.csv')
data1=pd.read_csv('final1.csv')

data['hfatigue']=data1['hfatigue']
data['vfatigue']=data1['vfatigue']
data.pop('Unnamed: 0')

names=f.get_names(data)
print(names)
data=data.dropna()

data=data.drop(['Date','Season','hgoal','vgoal','goaldiff','home','visitor','FT'],1)

data.to_csv('finall.csv',index=False)
y=data.pop('result')
x=data
print(data.columns)

train_features, test_features, train_labels, test_labels = train_test_split(x, y, test_size = 0.2, random_state = 2)

clf= NuSVC()

train_features=preprocessing.scale(train_features)
train_features=preprocessing.normalize(train_features)

clf.fit(train_features,train_labels)

# test model
predictions = clf.predict(pred)
cc=accuracy_score(test_labels,predictions)
print(cc)

home,draw,away=0,0,0
for x in predictions:
    if x==1:
        home+=1
    elif x==0:
        draw+=1
    else:
        away+=1

print(home/len(predictions),', ',home)
print(draw/len(predictions),', ',draw)
print(away/len(predictions),', ',away,'\n',f.winrates(data1))
# accuracy


