import requests
from requests_ntlm import HttpNtlmAuth
import base64
import os
#-------------------------------------------------------------------------------------------
# A convenience class provides methods to set fields values of TFS item and method to
#  report TFS item
#
# bsiclass                                                 Ridha.Malik   11/2017
#-------------------------------------------------------------------------------------------

class TFS:
    
    #------------------------------------------------------------------------------------------- 
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------
    def __init__(self):
        self.dict_field={}
        self.list_field=[]
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/System.AreaPath"
        self.dict_field['value']="Platform Technology\DgnDb Platform (2249)\iModel Tools"
        self.check_attribute_exists("/fields/Target Release")
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/Target Release"
        self.dict_field['value']="DgnClientSdk"
        self.list_field.append(self.dict_field.copy())
    #-------------------------------------------------------------------------------------------
    # Use this method when want to report tfs using account credentials 
    # bsimethod                                           Ridha.Malik   12/2017
    #-------------------------------------------------------------------------------------------
    def set_credentials(self,username,password):
        self.username=username
        self.password=password
        
    #-------------------------------------------------------------------------------------------
    # Get account username
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_username(self):
        return self.username

    #-------------------------------------------------------------------------------------------
    # Get account password
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_password(self):
        return self.password
    
    #-------------------------------------------------------------------------------------------
    # Use this method when want to report tfs using personal access token
    # bsimethod                                           Ridha.Malik   12/2017
    #-------------------------------------------------------------------------------------------
    def set_accesstoken(self,accesstoken):
        accesstoken=":"+accesstoken
        self.accesstoken=base64.b64encode(accesstoken.encode('utf-8'))

    #-------------------------------------------------------------------------------------------
    # get accesstoken
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_accesstoken(self):
        return self.accesstoken
            
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------
    def set_title(self,title):
        self.check_attribute_exists("/fields/System.Title")
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/System.Title"
        self.dict_field['value']=title
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get title
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_title(self):
        value=self.getvaluefromlist("/fields/System.Title")
        return value
    
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   11/2017
    #------------------------------------------------------------------------------------------- 
    def set_areapath(self,areapath):
        self.check_attribute_exists("/fields/System.AreaPath")
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/System.AreaPath"
        self.dict_field['value']=areapath
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get area path
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_areapath(self):
        value=self.getvaluefromlist("/fields/System.AreaPath")
        return value
    
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------                            
    def set_iterationpath(self,iterationpath):
        self.check_attribute_exists("/fields/System.IterationPath")
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/System.IterationPath"
        self.dict_field['value']=iterationpath
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get iterationpath
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_iterationpath(self):
        value=self.getvaluefromlist("/fields/System.IterationPath")
        return value        
  
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------                            
    def set_foundin(self,foundin):
        self.check_attribute_exists("/fields/Found In")
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/Found In"
        self.dict_field['value']=foundin
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get foundin
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_foundin(self):
        value=self.getvaluefromlist("/fields/Found In")
        return value 
    
    #-------------------------------------------------------------------------------------------
    # Provide requestor name is sperated by space e.g  Ridha Malik insted of Ridha.Malik
    #
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------                             
    def set_requestor(self,requestor):
        self.check_attribute_exists("/fields/Requestor")
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/Requestor"
        self.dict_field['value']=requestor
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get requestor
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_requestor(self):
        value=self.getvaluefromlist("/fields/Requestor")
        return value 
    
    #-------------------------------------------------------------------------------------------
    # Provide approver name is sperated by space e.g  Ridha Malik insted of Ridha.Malik
    #
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------                              
    def set_approver(self,approver):
        self.check_attribute_exists("/fields/Approver")
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/Approver"
        self.dict_field['value']=approver
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get approver
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_approver(self):
        value=self.getvaluefromlist("/fields/Approver")
        return value
    
    #-------------------------------------------------------------------------------------------
    # Provide developer name is sperated by space e.g  Ridha Malik insted of Ridha.Malik
    #
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------                            
    def set_developer(self,developer):
        self.check_attribute_exists("/fields/Developer")        
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/Developer"
        self.dict_field['value']=developer
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get developer
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_developer(self):
        value=self.getvaluefromlist("/fields/Developer")
        return value
    
    #-------------------------------------------------------------------------------------------
    # Provide tester name is sperated by space e.g  Ridha Malik insted of Ridha.Malik
    #
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------                          
    def set_tester(self,tester):
        self.check_attribute_exists("/fields/Tester")      
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/Tester"
        self.dict_field['value']=tester
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get tester
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_tester(self):
        value=self.getvaluefromlist("/fields/Tester")
        return value

    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------                           
    def set_team(self,team):
        self.check_attribute_exists("/fields/Team")       
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/Team"
        self.dict_field['value']=team
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get team
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_team(self):
        value=self.getvaluefromlist("/fields/Team")
        return value

    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------                           
    def set_steps_to_reproduce(self,steps):
        self.check_attribute_exists("/fields/Microsoft.VSTS.TCM.ReproSteps") 
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/Microsoft.VSTS.TCM.ReproSteps"
        self.dict_field['value']=steps
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get steps to reproduce
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_steps_to_reproduce(self):
        value=self.getvaluefromlist("/fields/Microsoft.VSTS.TCM.ReproSteps")
        return value
    
    #-------------------------------------------------------------------------------------------
    # To set Multiple Tags on TFS item pass tag value comma separated
    #
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------                           
    def set_tag(self,tag):
        self.check_attribute_exists("/fields/Tags")
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/Tags"
        self.dict_field['value']=tag
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get Tag
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_tag(self):
        value=self.getvaluefromlist("/fields/Tags")
        return value
    
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------                            
    def set_targetrelease(self,targetrelease):
        self.check_attribute_exists("/fields/Target Release")
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/Target Release"
        self.dict_field['value']=targetrelease
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get targetrelease
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_targetrelease(self):
        value=self.getvaluefromlist("/fields/Target Release")
        return value
    
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   05/2018
    #-------------------------------------------------------------------------------------------
    def set_history(self,history):
        self.dict_field['op']="add"
        self.dict_field['path']="/fields/System.History"
        self.dict_field['value']=history
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get history
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_history(self):
        value=self.getvaluefromlist("/fields/System.History")
        return value

    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   05/2018
    #-------------------------------------------------------------------------------------------
    def set_hyperlink(self,hyperlink):
        self.checkvalue_exits_inrelations("Hyperlink")
        self.dict_field['op']="add"
        self.dict_field['path']="/relations/-"
        value={}
        value["rel"]="Hyperlink"
        value["url"]=str(hyperlink)
        self.dict_field['value']=value
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get hyperlink
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_hyperlink(self):
        value=self.getvaluefromrelations("Hyperlink")
        return value
    
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   05/2018
    #-------------------------------------------------------------------------------------------
    def set_link(self,link):
        self.checkvalue_exits_inrelations("/relations/-")
        self.dict_field['op']="add"
        self.dict_field['path']="/relations/-"
        value={}
        value["rel"]="System.LinkTypes.Dependency-forward"
        value["url"]=str(link)
        self.dict_field['value']=value
        self.list_field.append(self.dict_field.copy())
        
    #-------------------------------------------------------------------------------------------
    # get link
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def get_link(self):
        value=self.getvaluefromrelations("System.LinkTypes.Dependency-forward")
        return value
    
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   12/2017
    #-------------------------------------------------------------------------------------------
    def checkcredentials(self):
        if not ((hasattr(self,"username") and hasattr(self,"password"))or hasattr(self,"accesstoken")):
            print "set username and password or personal access token these are compulsory for file tfs item "
            return False
        return True
    
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   12/2017
    #-------------------------------------------------------------------------------------------                            
    def checkrequiredattributes(self):
        if not ((hasattr(self,"username") and hasattr(self,"password"))or hasattr(self,"accesstoken")):
            print "set username and password or personal access token these are compulsory for file tfs item "
            return False
        if not(any( "System.Title" in d['path'] and bool(d['value']) for d in self.list_field) and any( "Found In" in d['path'] and bool(d['value'])  for d in self.list_field) and any( "System.AreaPath" in d['path'] and bool(d['value'])  for d in self.list_field)):
            print "set title, found in and areapath attribute these are compulsory for file tfs item "
            return False
        return True
    
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def check_attribute_exists(self,attribute):
        i=0
        for d in self.list_field:
            if (attribute in d['path']):
                self.list_field.pop(i)
            i=i+1
            
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def getvaluefromlist(self,attribute):
        i=0
        for d in self.list_field:
            if (attribute in d['path']):
                return self.list_field[i]['value']
            i=i+1
            
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def getvaluefromrelations(self,rel):
        i=0
        for d in self.list_field:
            if ("/relations/-" in d['path'] and d['value']['rel']==rel):
                return self.list_field[i]['value']
            i=i+1
            
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------
    def checkvalue_exits_inrelations(self,rel):
        i=0
        for d in self.list_field:
            if ("/relations/-" in d['path'] and d['value']['rel']==rel):
                self.list_field.pop(i)
            i=i+1
            
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   11/2017
    #-------------------------------------------------------------------------------------------   
    def report_tfsitem(self):
        status=self.checkrequiredattributes()
        if status:
            self.checkvalue_exits_inrelations("AttachedFile")
            tfsApi = 'http://tfs.bentley.com:8080/tfs/ProductLine/Platform%20Technology/_apis/wit/workitems/$Defect?api-version=1.0'
            if hasattr(self,"username") and hasattr(self,"password"):
                headers = {'Content-Type': 'application/json-patch+json'}
                tfsResponse = requests.patch(tfsApi,auth=HttpNtlmAuth(self.username,self.password),json=self.list_field,headers=headers)
            elif hasattr(self,"accesstoken"):
                print self.list_field
                headers = {'Content-Type': 'application/json-patch+json',
                          'Authorization': 'Basic '+self.accesstoken
                          }
                tfsResponse = requests.patch(tfsApi,json=self.list_field,headers=headers)
            else :
                  print "Set required parameters"
                  return -1
            if(tfsResponse.ok):
                tfsResponse = tfsResponse.json()
                print "### Tfs id",tfsResponse.get('id')
                return tfsResponse.get("id")
            else:
                print "Fail to report tfs status code:",tfsResponse.status_code
                return -1
        else:
             print "Fail to report tfs"
             return -1
   
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   05/2018
    #-------------------------------------------------------------------------------------------                            
    def UploadAttachment(self,filename,uploadedfilemane):
        status=self.checkcredentials()
        if status:
            if os.path.exists(filename):
                uploadapi ='http://tfs.bentley.com:8080/tfs/ProductLine/_apis/wit/attachments?fileName='+uploadfilemane+'&api-version=1.0'
                print uploadapi
                if hasattr(self,"username") and hasattr(self,"password"):
                    headers = {'Content-Type': 'application/json'}
                    auth="ntlm"
                else:
                    headers = {'Content-Type': 'application/json',
                               'Authorization': 'Basic '+self.accesstoken
                               }
                    auth="accesstoken"
                if filename.endswith(".7z")or filename.endswith(".zip"):
                    fileobj = open(filename, 'rb')
                    if auth=="ntlm":
                        tfsResponse = requests.post(uploadapi,auth=HttpNtlmAuth(self.username,self.password),headers=headers,data={"mysubmit":"Go"},files={"archive": (filename, fileobj)})
                    else:
                        tfsResponse = requests.post(uploadapi,headers=headers,data={"mysubmit":"Go"},files={"archive": (filename, fileobj)})
                else:
                    data = open(filename, 'rb').read()
                    if auth=="ntlm":
                        tfsResponse = requests.post(uploadapi,auth=HttpNtlmAuth(self.username,self.password),data=data,headers=headers)
                    else:
                        tfsResponse = requests.post(uploadapi,data=data,headers=headers)
                if(tfsResponse.ok):
                    tfsResponse = tfsResponse.json()
                    return tfsResponse.get("url")
                else:
                    print "Fail to upload attachment on tfs status code:",tfsResponse.status_code
                    return -1
            else:
                print "Filepath is not exists"
                return -1
        else:
            return -1
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   05/2018
    #-------------------------------------------------------------------------------------------                            
    def GetWorkItem(self,workitemno):
        status=self.checkcredentials()
        if status:
            tfsapi ='http://tfs.bentley.com:8080/tfs/ProductLine/_apis/wit/workitems/'+str(workitemno)+"?api-version=1.0"
            if hasattr(self,"username") and hasattr(self,"password"):
                tfsResponse = requests.get(tfsapi,auth=HttpNtlmAuth(self.username,self.password))
            else:
                headers = {'Authorization': 'Basic '+self.accesstoken}
                tfsResponse = requests.get(tfsapi,headers=headers)
            if(tfsResponse.ok):
                tfsResponse = tfsResponse.json()
                return tfsResponse
            else:
                print "Fail to get workitem from tfs and its status code:",tfsResponse.status_code
                return -1
        else:
            return -1     
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   05/2018
    #-------------------------------------------------------------------------------------------                            
    def AddAttachmentToWorkItem(self,attachmenturl,workitemno):
        status=self.checkcredentials()
        result=self.checkvalue_exits_inrelations("AttachedFile")
        self.dict_field['op']="add"
        self.dict_field['path']="/relations/-"
        value={}
        value["rel"]="AttachedFile"
        value["url"]=str(attachmenturl)
        self.dict_field['value']=value
        self.list_field.append(self.dict_field.copy())
        if status:
            uploadapi ="http://tfs.bentley.com:8080/tfs/ProductLine/_apis/wit/workitems/"+str(workitemno)+"?api-version=1.0"
            print uploadapi
            if hasattr(self,"username") and hasattr(self,"password"):
                headers = {'Content-Type':'application/json-patch+json'}
                tfsResponse = requests.patch(uploadapi,auth=HttpNtlmAuth(self.username,self.password),json=self.list_field,headers=headers)
            else :
                headers = {'Content-Type': 'application/json-patch+json',
                          'Authorization': 'Basic '+self.accesstoken
                          }
                tfsResponse = requests.patch(uploadapi,json=self.list_field,headers=headers)
            if(tfsResponse.ok):
                tfsResponse = tfsResponse.json()
                return tfsResponse.get("id")
            else:
                print "Fail to report tfs status code:",tfsResponse.status_code
                return -1
        else:
             return -1
            
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   05/2018
    #-------------------------------------------------------------------------------------------                            
    def UpdateWorkItem(self,workitemno):
        status=self.checkcredentials()
        if status:
            uploadapi ="http://tfs.bentley.com:8080/tfs/ProductLine/_apis/wit/workitems/"+str(workitemno)+"?api-version=1.0"
            print uploadapi
            if hasattr(self,"username") and hasattr(self,"password"):
                headers = {'Content-Type':'application/json-patch+json'}
                tfsResponse = requests.patch(uploadapi,auth=HttpNtlmAuth(self.username,self.password),json=self.list_field,headers=headers)
            else :
                headers = {'Content-Type': 'application/json-patch+json',
                          'Authorization': 'Basic '+self.accesstoken
                          }
                tfsResponse = requests.patch(uploadapi,json=self.list_field,headers=headers)
            if(tfsResponse.ok):
                tfsResponse = tfsResponse.json()
                return tfsResponse.get("id")
            else:
                print "Fail to report tfs status code:",tfsResponse.status_code
                return -1
        else:
             return -1
    #-------------------------------------------------------------------------------------------
    # bsimethod                                           Ridha.Malik   06/2018
    #-------------------------------------------------------------------------------------------                            
    def GetWorkItemStatus(self,workitemno):
        status=self.checkcredentials()
        if status:
            tfsapi ='http://tfs.bentley.com:8080/tfs/ProductLine/_apis/wit/workitems/'+str(workitemno)+"?fields=System.State&api-version=1.0"
            if hasattr(self,"username") and hasattr(self,"password"):
                tfsResponse = requests.get(tfsapi,auth=HttpNtlmAuth(self.username,self.password))
            else:
                headers = {'Authorization': 'Basic '+self.accesstoken}
                tfsResponse = requests.get(tfsapi,headers=headers)
            if(tfsResponse.ok):
                tfsResponse = tfsResponse.json()
                return tfsResponse['fields']['System.State']
            else:
                print "Fail to get workitem status from tfs and its status code:",tfsResponse.status_code
                return -1
        else:
            return -1   