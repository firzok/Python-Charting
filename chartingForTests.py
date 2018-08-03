# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:47:56 2018

@author: Firzok.Nadeem
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from SqliteDatabase import Database
import datetime
import argparse







def StreamId(c,Stream):
    '''
        Retruns the stream Id from database
    '''
    c.execute("SELECT  StreamId FROM Stream WHERE name = ?",(Stream ,))
    result = c.fetchall()
    if len(result) != 0:
        id=result[0][0]
        return id
    else:
        print "Stream doesnot exists in testcatalog"
        exit (0)



def valid_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date its format YYYY-MM-DD should be: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)
        
       
        
db=Database("TestsCatalog.db")
db.connectDatabase()

c=db.cursor
#Find Stream id
streamid=StreamId(c,Stream)
sql="SELECT TestId, TestCase, Test, Author, Component, Date FROM  Tests WHERE StreamId ="+str(streamid)+" AND Date BETWEEN "+'\''+StartDate+'\''+" AND "+'\''+EndDate+'\''
c.execute(sql)
data=c.fetchall()
#report=os.path.join(*[srcpath,"DgnDbTestingScripts","TestFlakiness","NewlyAddedTestsReport.csv"])
report = "TestsReport.csv"
if len(data)!=0:
    if os.path.exists(report):
        os.remove(report)
    with open(report , "wb") as f:
        writer = csv.writer(f)
        writer.writerow(('TestCase','TestName','Author','Component','Date'))
        for x in data:
            writer.writerow((x[1],x[2],x[3],x[4],x[5]))
    print "Report Generated"
    exit(0)
else:
    print "Doesn't find any New Tests"
    exit(0)





df=pd.read_csv("NewlyAddedTestsReport.csv")
data = np.unique(df.Component, return_counts=True)

sData = zip(*sorted(zip(data[1], data[0])))
Y, X = sData
X = np.array(X)
Y = np.array(Y)
size = np.shape(X)[0]


#Main Graph
fig = plt.figure(figsize=(size+5,size))
sns.set_style("whitegrid")

colors = sns.color_palette("cubehelix", len(df.Component.unique()) + 10)

for i in range(size):
    g = sns.barplot(y=X[i:i+1], x=Y[i:i+1], color=colors[i], order = X, url = X[i]+'.svg', orient='h')
    g.text(Y[i] + 3, i + 0.1, Y[i], color='black', ha="center", weight="bold")

g.set_title("Tests added between ___ and ___")
sns.despine(left=True)
plt.savefig("TEST2/test1.svg")



#Sub Graphs
for i in df.groupby('Component'):
    fig = plt.figure(figsize=(size,size+2))
    sns.set_style("whitegrid")
    name = i[0]
    print name,
    X, Y = np.unique(i[1].Author, return_counts=True)
    sData = zip(*sorted(zip(Y, X)))
    Y, X = sData
    X = np.array(X)
    Y = np.array(Y)
    colors = sns.color_palette("cubehelix", len(X) + 3)
    
    g = sns.barplot(y=X, x=Y, palette=colors, order = X, orient='h')
    for i in range(np.shape(X)[0]):
        g.text(Y[i] + 0.5, i + 0.02, Y[i], color='black', ha="center", weight="bold")
    g.set_title(name)
    sns.despine(left=True)
    plt.savefig("TEST2/"+name+".svg")
    
    
    
    
    
#*************************************************************************************************************
    
    
    







