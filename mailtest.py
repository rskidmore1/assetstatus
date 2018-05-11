from mail import * 
import email 
from email.parser import Parser



parser = Parser()

acctID = ''

def mailTest(): 
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

  #Gets email body 
  email = parser.parsestr(raw_email)



  bodytext=email.get_payload()[0].get_payload()
  if type(bodytext) is list:
    bodytext=','.join(str(v) for v in bodytext)

  #print bodytext






  def getName(): 
  
    #Creating getName method 
    num = bodytext.index('ID')
    start = num + 3 

    stop = start + 18
    
    #Add 15 char to end of ID 
    acctID = bodytext[start:stop]
    print acctID
 
  def checkName():
    subject = email.get('Subject')
    print subject 

  '''
    if subject == 'FW: Order Notification' or 'Fw: Order Notification':
      print 'The script works'
      getName()
    else: 
      print "Not the Notification email"
    print subject 
    print ''
    print "End of checkName and getName script" 
  '''

  checkName()
  


mailTest() 
