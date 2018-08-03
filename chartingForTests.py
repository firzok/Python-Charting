import os
import csv
import sys
import sqlite3
import argparse
import datetime
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Common Scripts to be used by any task
srcpath = os.getenv('SrcRoot')
commonScriptsDir = os.path.join(srcpath, 'DgnDbTestingScripts', 'CommonTasks')
sys.path.append(commonScriptsDir)
dppath=os.path.join(*[srcpath,"DgnDbTestingScripts","TestFlakiness","TestsCatalog.db"])

import FindStream
from SqliteDatabase import Database


#-------------------------------------------------------------------------------------------
# bsimethod                                     Ridha.Malik                    07/2018
#-------------------------------------------------------------------------------------------
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
        
#-------------------------------------------------------------------------------------------
# bsimethod                                     Ridha.Malik                    07/2018
#-------------------------------------------------------------------------------------------
def valid_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date its format YYYY-MM-DD should be: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)
        
        
        
#Stream = "bim0200"
#StartDate="2017-09-01"
StartDate=datetime.date.strftime(StartDate, "%Y-%m-%d")
#EndDate="2018-07-01"
EndDate=datetime.date.strftime(EndDate, "%Y-%m-%d") 
        


db=Database("TestsCatalog.db")
db.connectDatabase()
c=db.cursor
streamid=StreamId(c,Stream)



months = pd.date_range(start = StartDate, end = EndDate, freq='M', normalize=False).date



streamid=StreamId(c,Stream)
sql = 'SELECT component, COUNT(*) FROM Tests where StreamId == ' + str(streamid) + ' AND Date <' + '\'' + StartDate + '\'' + 'GROUP BY component;'
c.execute(sql)
data=c.fetchall()
if len(data) == 0:
    print "No Test added prior to "+StartDate
df = pd.DataFrame.from_records(data, columns=['Component', 'Prior Count'])




for m in months:
    sql = 'SELECT component, COUNT(*) FROM Tests where StreamId == ' + str(streamid) + " AND Date < '" + str(m) + "' GROUP BY component;"
    c.execute(sql)
    data=c.fetchall()
    df0 = pd.DataFrame.from_records(data, columns=['Component', 'Count'+str(m.month)+"-"+str(m.year)])
    
    df = pd.merge(df, df0, on='Component', how='outer')
    df.fillna(0, inplace=True)
    
    
    
# style
plt.style.use('seaborn-darkgrid')
 
# create a color palette
cmap = plt.get_cmap('nipy_spectral')
colors = [cmap(i) for i in np.linspace(0, 1, len(df))]    







#Create the main page graph
plt.figure(figsize=(25,15))
plt.subplot(2, 1, 1)

# multiple line plot
for i, row in df.iterrows():
#     print row
    plt.plot(row[1:], label = row[0], color = colors[i], linewidth = 2.0)
#     p.set_urls(['http://www.bbc.co.uk/news', 'http://www.google.com', None])

    # Add legend    
plt.legend(loc='upper left', ncol=1, fontsize=15, bbox_to_anchor=(1, 1))



# # Add titles
plt.title("New Tests added between "+StartDate+" and "+EndDate, fontsize=25, fontweight=0.5, color='Black')
plt.xlabel("Time Frame", fontsize=20)
plt.ylabel("Tests", fontsize=20)

x=['Prior Tests'] 
x.extend(months)

plt.xticks(np.arange(len(x)), x, fontsize=20)
plt.yticks(fontsize=20)


plt.subplot(2, 1, 2)



df1=pd.read_csv("NewlyAddedTestsReport.csv")
data = np.unique(df1.Component, return_counts=True)

sData = zip(*sorted(zip(data[1], data[0])))
Y, X = sData
X = np.array(X)
Y = np.array(Y)

size = np.shape(X)[0]

# fig = plt.figure(figsize=(size+5,size))
sns.set_style("whitegrid")

colors = sns.color_palette("cubehelix", len(df1.Component.unique()) + 10)

for i in range(size):
    g = sns.barplot(y=X[i:i+1], x=Y[i:i+1], color=colors[i], order = X, url = X[i]+'.svg', orient='h')
    g.text(Y[i] + 3, i + 0.1, Y[i], color='black', ha="center", weight="bold")
    g.text(2, i + 0.1, Y[i], color='black', ha="center", weight="bold")


sns.despine(left=True)
g.tick_params(labelsize=20)
plt.savefig('Report/Main.svg', dpi=300, orientation='landscape')










#Create the secondary graphs
for i in df1.groupby('Component'):
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
    plt.savefig("Report/"+name+".svg")



