# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:46:07 2020

"""

import numpy as np 
import pandas as pnd
import scipy as sp 
import ast
import matplotlib.pyplot as plt #data visualisation
import seaborn as sb
import statsmodels.formula.api as sm #running stats functions
from datetime import datetime #date and time convertor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

docrep=pnd.read_csv("C:\Revolut_Challenge_Prakhyath\doc_reports_sample.csv")

#docrep.head()
#docrep.shape()

facerep=pnd.read_csv("C:\Revolut_Challenge_Prakhyath\\face_reports_sample.csv")
#facerep.head()
#facerep.shape()v

#groupby('user_id')[''].value_counts().reset_index().sort_values('user_id')
#facegrp=facerep.groupby('user_id')['result'].value_counts().reset_index().sort_values('user_id')

#docgrp=docrep.groupby("user_id").sort_values('user_id')
#docgrp = docgrp.agg({"result": "nunique"}).sort_values('user_id')
#docgrp = docgrp.reset_index()

propdfnew = pnd.DataFrame()
for index, row in docrep.iterrows():
    #print(type(row['properties']))
    dict=ast.literal_eval(row['properties'])
    #print(type(dict))
    #print(dict)
    for key in dict:
       # type(dict[key])
       propdfnew.at[index,'attempt_id']=row['attempt_id']
       propdfnew.at[index,'user_id']=row['user_id']
       propdfnew.at[index,key]=dict[key]



#docrep['result'].count().plot(linewidth=0.5)

#docgrp=docrep.groupby('created_at').value_counts('result')

#sb.set()
#sb.load_dataset("docrep")

#sb.relplot(x="created_at", y="result", col="align",
#            hue="choice", size="coherence", style="choice",
#            facet_kws=dict(sharex=False),
#            kind="line", legend="full", data=docrep);
           
#g=sb.countplot(x="created_at", hue="result", data=docrep)


#docrep.plot('result')
#plt.show()
