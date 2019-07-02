#! /usr/bin/python3

import functions

file=functions.clean('USA.csv')

a=functions.create_goaldiff(file)
file['goaldiff']=a

b=functions.create_results(file)
file['result']=b

file.to_csv('usa_worked.csv')
