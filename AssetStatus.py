from mail import * 
from api import * 
from datetime import date
import datetime  
import schedule
import time 
import threading 
import email 
import json 
from email.parser import Parser
parser = Parser()




#init vars
IMEI = ''
bodytext = ''
IMEIs = [] 

def assetChange(): #Main class
  mail.list() #Gets all emails 
  mail.select("inbox") # Gets inbox (instead of like "sent")



  result, data = mail.search(None, "ALL") #Gets "all" emails, I think maybe
 
  ids = data[0] # data is a list.
  id_list = ids.split() # ids is a space separated string 
  latest_email_id = id_list[-1] # get the latest
 
  result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
  raw_email = data[0][1]

  #print raw_email

  with open('data.txt', 'w') as outfile:
      json.dump(raw_email, outfile)
  global bodytext
  #Gets email body 
  email = parser.parsestr(raw_email)



  bodytext=email.get_payload()[0].get_payload()
  if type(bodytext) is list:
    bodytext=','.join(str(v) for v in bodytext)




  def getIMEI(): #Gets IMEI from email  
    
    #Creating getIMEI method 
    num = bodytext.index('ay:') #Line before IMEIs in email 
    #print bodytext 
    start = num + 4
    print len(bodytext) - num
    endOfString = len(bodytext) - num

    stop = start + endOfString
    
    global IMEI  
    global IMEIs  
    IMEI = bodytext[start:stop]
    IMEI = IMEI.strip()
    acctIdByLine =  IMEI.splitlines()
    for x in acctIdByLine: 
      #print x
      if x.startswith('35'): 
        print x[0:15]
        IMEIs.append(x[0:15]) 
    print IMEIs 

 
  def checkName():
    subject = email.get('Subject')

    if subject == 'FW: Device Status Change' or subject == 'Fw: Device Status Change':  #checks subject of Asset Status Email 
      print 'The script works'
      getIMEI()
    else: 
      print "Not the Asset Change email  email"
    print ''

  checkName()
   
  print 'IMEI: '  + IMEI 

  
  for imei in IMEIs:
    query = sf.query("SELECT Id FROM Asset WHERE Name = '%s'" % imei )
    print "query"
    #print query['OrderedDict']
    jsonquery = json.dumps(query)
    loads = json.loads(jsonquery)
    IdRaw = loads['records'][0]['Id']
    print IdRaw[0:15]
    Idtrim = IdRaw[0:15]
    today = date.today().isoformat()
    assetStatus = sf.Asset.update(Idtrim, {'Status': 'Active'})
    StatusDate = sf.Asset.update(Idtrim, {'InstallDate':  today}) 
    print ''
    
   
assetChange()


