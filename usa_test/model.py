#! /usr/bin/python3

import functions as f
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import BaggingClassifier
#from sklearn.neural_network import MLPClassifier
from sklearn.svm import NuSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv('final_usa.csv')
data1=data
data.pop('Unnamed: 0')

names=f.get_names(data)
print(names)
home=data.loc[data['home']=='Los Angeles Galaxy'][-1:]
home=home.drop(['vfatigue','vavg_diff50','vavg_diff5','vavg_points15','vavg_points5'],1)

away=(data.loc[data['visitor']=='Toronto FC'][-1:])
away=away.drop(['hfatigue','havg_diff50','havg_diff5','havg_points15','havg_points5'],1)

data=data.dropna()

data=data.drop(['Date','hgoal','vgoal','goaldiff','home','visitor'],1)

y=data.pop('result')
x=data
x=x.drop(['vfatigue', 'vavg_diff50', 'vavg_diff5','vavg_points15', 'vavg_points5'],1)
print(data.columns)

away=away.drop(['result','Date','hgoal','vgoal','goaldiff','home','visitor'],1)
print(away)#['vfatigue','vavg_diff50','vavg_diff5','vavg_points15','vavg_points5'])
home=home.drop(['result','Date','hgoal','vgoal','goaldiff','home','visitor'],1)
home=home.reset_index(drop=True)
away=away.reset_index(drop=True)
print(home)#['vfatigue','vavg_diff50','vavg_diff5','vavg_points15','vavg_points5'])

pred = pd.concat([home,away],axis =1,join = 'inner', sort=False)
train_features, test_features, train_labels, test_labels = train_test_split(x, y, test_size = 0.2, random_state = 2)

from sklearn.model_selection import GridSearchCV

param_grid = {
        'random_state':[10,20]
    #'max_depth': [20,40],
    #'n_estimators': [200,300,400]
}
#clf= MLPClassifier(activation='logistic',solver='adam',batch_size=8)
clf= NuSVC()
grid_search = GridSearchCV(estimator = clf, param_grid = param_grid, 
                          cv = 3, n_jobs=-1, verbose = 2)
train_features=preprocessing.scale(train_features)
train_features=preprocessing.normalize(train_features)

grid_search.fit(train_features, train_labels)
print(grid_search.best_params_)
grid_search=grid_search.best_estimator_
#clf.fit(train_features,train_labels)

print(pred)
pred=preprocessing.normalize(pred)
pred=preprocessing.scale(pred)

# test model
predictions = grid_search.predict(test_features)
#predictions = clf.predict(pred)
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


