import os
import csv
import sys
import shutil
import datetime
import argparse
import numpy as np
import pandas as pd
import seaborn as sns
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
        




#-------------------------------------------------------------------------------------------
# bsimethod                                     Firzok.Nadeem                    08/2018
#-------------------------------------------------------------------------------------------
def createChartsForUnknown():
    sns.reset_defaults()
    plt.clf()
    print "\nCreating charts for Unknown...",
    sql = "SELECT Component, count(*) FROM Tests WHERE Author = 'UnKnown' and StreamId = "+str(streamid)+" and Date BETWEEN '"+StartDate+"' AND '"+EndDate+"' group by Component;"
    c.execute(sql)
    data=c.fetchall()
    if len(data) == 0:
        print "No Test added prior to "+StartDate
    df2 = pd.DataFrame.from_records(data, columns=['Component', 'Count'])


    X = np.array(df2.Component)
    Y = np.array(df2.Count)

    size = np.shape(X)[0]
    
    sns.set_style("whitegrid")

    colors = sns.color_palette("cubehelix", len(df2.Component.unique()) + 5)

    # print size
    for i in range(size):
        g = sns.barplot(y=X[i:i+1], x=Y[i:i+1], color=colors[i], order = X, url = X[i]+'-unknown.html', orient='h')
        g.text(Y[i] + 0.5, i, Y[i], color='black', ha="center", weight="bold")
        g.tick_params(labelsize=20)

    # sns.despine(left=True)
    
    plt.title("Tests added by Unknown Authors between "+StartDate+" and "+EndDate, fontsize=20, fontweight=0.5, color='Black')
    plt.savefig("Report/"+'Unknown.svg', dpi=300, bbox_inches="tight")

    
    for i in range(size):
       
        sql = "SELECT Date, Component, Test, TestCase, File FROM Tests WHERE Author = 'UnKnown' and StreamId = "+str(streamid)+" and Component='"+X[i]+"' AND Date BETWEEN '"+StartDate+"' AND '"+EndDate+"';"
        c.execute(sql)
        data=c.fetchall()
        if len(data) == 0:
            print "Unable to get data fo unknown test "+X[i]
        df2 = pd.DataFrame.from_records(data, columns=['Date', 'Component', 'Test', 'TestCase', 'File'])
    #     print df2.columns

        htmlString = '<table style="width: 50%;" border="3" cellpadding="20"><tbody><tr style="font-weight: bold; background-color: black; color: white;"><td>Index</td><td>Date</td><td>Component</td><td>Test</td><td>Test Case</td><td>File</td></tr>'
        
        for j, row in df2.iterrows():
            htmlString+="<tr><td>"+str(j+1)+"</td>"+"<td>"+row.values[0]+"</td>"+"<td>"+row.values[1]+"</td>"+"<td>"+row.values[2]+"</td>"+"<td>"+row.values[3]+"</td>"+"<td>"+row.values[4]+"</td></tr>"
        htmlString+="</tbody></table>"
        html_file = open("Report/"+X[i]+'-unknown.html','w')
        html_file.write(htmlString)
        html_file.close()
        print ".",






#-------------------------------------------------------------------------------------------
# bsimethod                                     Firzok.Nadeem                    08/2018
#-------------------------------------------------------------------------------------------
def createMainGraph(df):
    
    # style
    plt.style.use('seaborn-darkgrid')
    
    # create a color palette
    cmap = plt.get_cmap('nipy_spectral')
    colors = [cmap(i) for i in np.linspace(0, 1, len(df))]    

    #Create the main page graph
    plt.figure(figsize=(25,13))
    plt.subplot(3, 1, 1)

    # multiple line plot
    for i, row in df.iterrows():
        plt.plot(row[1:], label = row[0], color = colors[i], linewidth = 2.0)
    # Add legend    
    plt.legend(loc='upper left', ncol=1, fontsize=15, bbox_to_anchor=(1, 1))



    # # Add titles
    plt.title("Trend of new Tests added between "+StartDate+" and "+EndDate, fontsize=25, fontweight=0.5, color='Black')
    plt.xlabel("Time Frame", fontsize=20)
    plt.ylabel("Tests", fontsize=20)

    x=['Prior Tests'] 
    x.extend(months)

    plt.xticks(np.arange(len(x)), x, fontsize=20)
    plt.yticks(fontsize=20)


    plt.subplot(3, 1, 2)

    sql = 'SELECT TestId, TestCase, Test, Author, Component, Date FROM Tests where StreamId == ' + str(streamid) + " AND Date BETWEEN '"+StartDate+"' AND '"+EndDate+"'"
    c.execute(sql)
    data=c.fetchall()
    if len(data) == 0:
        print "No Test added between "+StartDate+" and "+EndDate
        exit(0)
    df1 = pd.DataFrame.from_records(data, columns=['TestId', 'TestCase', 'Test', 'Author', 'Component', 'Date'])

    data = np.unique(df1.Component, return_counts=True)
    Y, X = zip(*sorted(zip(data[1], data[0])))
    X = np.array(X)
    Y = np.array(Y)

    size = np.shape(X)[0]

    # fig = plt.figure(figsize=(size+5,size))
    sns.set_style("whitegrid")

    colors = sns.color_palette("cubehelix", len(df1.Component.unique()) + 10)

    print "Creating Main Graph..."
    for i in range(size):
        g = sns.barplot(y=X[i:i+1], x=Y[i:i+1], color=colors[i], order = X, url = "Secondary/"+X[i]+'.html', orient='h')
        g.text(Y[i] + 0.5, i + 0.1, Y[i], color='black', ha="center", weight="bold")
        


    sns.despine(left=True)
    g.tick_params(labelsize=20)

    plt.subplot(3, 1, 3)
    plt.title("For Charts by Unknown Author click me", fontsize=15, fontweight=15, color='Black', url='Unknown.html')

    g=sns.barplot(y=[0], x=[0], url ='Unknown.svg', orient='v', label="Unknown")
    g.set(yticks=[],xticks=[])

    plt.savefig('Report/Main.svg', dpi=300, orientation='landscape', bbox_inches="tight")
    return df1, size



#-------------------------------------------------------------------------------------------
# bsimethod                                     Firzok.Nadeem                    08/2018
#-------------------------------------------------------------------------------------------
def createSecondaryCharts(df1, size):
    print "Create the secondary graphs for :"
    #Create the secondary graphs
    for i in df1.groupby('Component'):
        fig = plt.figure(figsize=(size,size+2))
        sns.set_style("whitegrid")
        name = i[0]
        print "\n\t"+name
        X, Y = np.unique(i[1].Author, return_counts=True)
        sData = zip(*sorted(zip(Y, X)))
        Y, X = sData
        X = np.array(X)
        Y = np.array(Y)
        colors = sns.color_palette("cubehelix", len(X) + 3)
        os.mkdir("Report/Secondary/"+name)
        print "\tMaking html tables:\n\t\t",
        for i in range(np.shape(X)[0]):
            g = sns.barplot(y=X[i:i+1], x=Y[i:i+1], palette=colors, order = X, orient='h', url = name+"/"+X[i]+'.html')

            g.text(Y[i] + 0.5, i + 0.02, Y[i], color='black', ha="center", weight="bold")


            sql = "SELECT Date, Component, Test, TestCase, File FROM Tests WHERE Author = '"+X[i]+"' and StreamId = "+str(streamid)+" and Component='"+name+"' AND Date BETWEEN '"+StartDate+"' AND '"+EndDate+"';"
            c.execute(sql)
            data=c.fetchall()
            if len(data) == 0:
                print "Unable to get data fo unknown test "+X[i]
            df2 = pd.DataFrame.from_records(data, columns=['Date', 'Component', 'Test', 'TestCase', 'File'])
        #     print df2.columns
            htmlString = '<table style="width: 50%;" border="3" cellpadding="20"><tbody><tr style="font-weight: bold; background-color: black; color: white;"><td>Index</td><td>Date</td><td>Component</td><td>Test</td><td>Test Case</td><td>File</td></tr>'
            
            for j, row in df2.iterrows():
                htmlString+="<tr><td>"+str(j+1)+"</td>"+"<td>"+row.values[0]+"</td>"+"<td>"+row.values[1]+"</td>"+"<td>"+row.values[2]+"</td>"+"<td>"+row.values[3]+"</td>"+"<td>"+row.values[4]+"</td></tr>"
            htmlString+="</tbody></table>"
            html_file = open("Report/Secondary/"+name+"/"+X[i]+'.html','w')
            html_file.write(htmlString)
            html_file.close()
            print X[i],


        g.set_title(name)
        sns.despine(left=True)
        
        plt.savefig("Report/Secondary/"+name+".svg", bbox_inches="tight")







#-------------------------------------------------------------------------------------------
#                                                 Firzok.Nadeem                    08/2018
#-------------------------------------------------------------------------------------------
def convertFilesToHTML():
    dir = "Report"
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                if file.endswith(".svg"):
                    base = subdir+"\\"+file[:-4]
                    os.rename(subdir+"\\"+file, base + ".html")









#-------------------------------------------------------------------------------------------
#                                                 Firzok.Nadeem                    07/2018
#-------------------------------------------------------------------------------------------
#---Entry point of the Script ---#
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script generate report that tells about new tests added between a specified time span')
    parser.add_argument('-s','--stream' ,help='Stream name')
    parser.add_argument('-sd','--startdate',dest="StartDate",help='Starting date from where to find newly added tests - format YYYY-MM-DD',required=True,type=valid_date)
    parser.add_argument('-ed','--enddate',dest="EndDate",help='Find newly added tests till this date - format YYYY-MM-DD',required=True,type=valid_date)
    args = parser.parse_args()
    Stream = args.stream
    StartDate=args.StartDate
    StartDate=datetime.date.strftime(StartDate, "%Y-%m-%d")
    EndDate=args.EndDate
    EndDate=datetime.date.strftime(EndDate, "%Y-%m-%d") 


    if Stream == None:
        TeamConfigPath = os.path.join(os.getenv('SrcRoot'), 'teamConfig', 'treeConfiguration.xml')
        Stream = FindStream.FindStreamDetails(TeamConfigPath)
        Stream = Stream.lower()
    else:
         Stream = args.stream.lower()

    db=Database(dppath)
    # print dppath
    db.connectDatabase()
    c=db.cursor
    #Find Stream id
    streamid=StreamId(c,Stream)

    # Check if Report folder exist then delete it and create a new one
    if (os.path.isdir("Report")):
        print "Report folder already present deleting the contents..."
        shutil.rmtree('Report')
        os.mkdir('Report')
        os.mkdir('Report/Secondary')
    else:
        os.mkdir('Report')
        os.mkdir('Report/Secondary')

    months = pd.date_range(start = StartDate, end = EndDate, periods=5, normalize=False).date

    sql = 'SELECT component, COUNT(*) FROM Tests where StreamId == ' + str(streamid) + ' AND Date <' + '\'' + StartDate + '\'' + 'GROUP BY component;'
    c.execute(sql)
    data=c.fetchall()
    if len(data) == 0:
        print "No Test added prior to "+StartDate
        exit(0)
    df = pd.DataFrame.from_records(data, columns=['Component', 'Prior Count'])




    for m in months:
        sql = 'SELECT component, COUNT(*) FROM Tests where StreamId == ' + str(streamid) + " AND Date <= '" + str(m) + "' GROUP BY component;"
        c.execute(sql)
        data=c.fetchall()
        df0 = pd.DataFrame.from_records(data, columns=['Component', 'Count'+str(m)])
        
        df = pd.merge(df, df0, on='Component', how='outer')
        df.fillna(0, inplace=True)
    
    # Create Main Graphs
    df, size = createMainGraph(df)

    # Create Secondary Charts and html pages
    createSecondaryCharts(df, size)

    # Charts for Unknown
    createChartsForUnknown()

    # Convert files to html
    convertFilesToHTML()