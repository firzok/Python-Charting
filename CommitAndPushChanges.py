#--------------------------------------------------------------------------------------
#
#     $Source: CommonTasks/CommitAndPushChanges.py $
#
#  $Copyright: (c) 2018 Bentley Systems, Incorporated. All rights reserved. $
#
#--------------------------------------------------------------------------------------
import os
import sys
import argparse
import shutil

#-------------------------------------------------------------------------------------------
# bsimethod                                     Majd Uddin                     10/2017
#-------------------------------------------------------------------------------------------
def CommitAndPushMultipleFiles(filepath, fileNames, message, user=None):
    os.chdir(filepath)
    print "current",os.getcwd()
    os.system("hg status")
    status=1
    print status
    commitCmd = 'hg commit -m "' + message + '"'
    if user is not None:
        commitCmd = commitCmd + ' -u ' + user
    for file in fileNames:
        commitCmd = commitCmd + ' ' + file
    print 'Commit command is: ' + commitCmd
    status=os.system(commitCmd)
    print status
    if status==0:
       status=os.system("hg push")
       print "Push status",status
       if status!=0:
          stripstatus=os.system("hg strip tip")
          print "strip ",stripstatus
          updatetatus=os.system("hg pull -u")
          print "Pull and update status ",updatetatus
          return -1
       else:
           print "changes pushed successfully"
           return 0
    else:
        print "No changes found to commit"
        return 0


#-------------------------------------------------------------------------------------------
# bsimethod                                     Ridha.Malik                     10/2017
#-------------------------------------------------------------------------------------------
def CommitAndPush(filepath, filename, message, user=None):
    os.chdir(filepath)
    print "current",os.getcwd()
    os.system("hg status")
    status=1
    print status
    commitCmd="hg commit "+filename+" -m "+'"'+message+'"'
    if user is not None:
        commitCmd = commitCmd + ' -u ' +'"'+user+'"'
    status=os.system(commitCmd)
    print status
    if status==0:
       status=os.system("hg push")
       print "Push status",status
       if status!=0:
          stripstatus=os.system("hg strip tip")
          print "strip ",stripstatus
          updatetatus=os.system("hg pull -u")
          print "Pull and update status ",updatetatus
          return -1
       else:
           print "changes pushed successfully"
           return 0
    else:
        print "No changes found to commit"
        return 0


#-------------------------------------------------------------------------------------------
# bsimethod                                     Ridha.Malik                     10/2017
#-------------------------------------------------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tests Database.')

    parser.add_argument('--filepath',help='File path',required=True)
    parser.add_argument('--filename' ,help='File name want to commit and push',required=True)
    parser.add_argument('--message',help="Commit message",required=True)
    args = parser.parse_args()
    filepath=args.filepath
    filename=args.filename
    message=args.message
    CommitAndPush(filepath,filename,message)
    exit(0)
    
