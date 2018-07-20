#--------------------------------------------------------------------------------------
#
#     $Source: TestFlakiness/FindTestAddedBetweenIteration.py $
#
#  $Copyright: (c) 2018 Bentley Systems, Incorporated. All rights reserved. $
#
#--------------------------------------------------------------------------------------
import os
import csv
import sys
import sqlite3
import argparse
import datetime

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


    
#---Entry point of the Script ---#
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script generate report that tells about new tested added between specified time span')
    parser.add_argument('--stream' ,help='Stream name')
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
    db.connectDatabase()
    c=db.cursor
    #Find Stream id
    streamid=StreamId(c,Stream)
    sql="SELECT TestId, TestCase, Test, Author, Component, Date FROM  Tests WHERE StreamId ="+str(streamid)+" AND Date BETWEEN "+'\''+StartDate+'\''+" AND "+'\''+EndDate+'\''
    c.execute(sql)
    data=c.fetchall()
    report=os.path.join(*[srcpath,"DgnDbTestingScripts","TestFlakiness","NewlyAddedTestsReport.csv"])
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
