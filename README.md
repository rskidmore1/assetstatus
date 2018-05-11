Synopsis
AssetChange reads "Asset Change" emails, indicating that a device has activated and will be changed in SFDC automatically, that come into a specific email in box and mark the corresponding Asset "Active" in the indicated Salesforce.com instance. 


Install 
Use Python 2.7.6. Add the proper IMAP info to mail.py and Salesforce API credentials to api.py. Some variables will need to be changed in mecha.py most importantly the report ID in the url in the "report" variable value that indicates what report mecha.py is accessing. 

Tests
To test that the email inbox and Salesforce API are working using mailtest.py and sfdctest.pys. 

License
All properties belong to Ryan Skidmore. ryan.skidmore@yahoo.com. +19492664664

    .__________________________.
    | .___________________. |==|
    | |     Apple ][      | |  |
    | |                   | |  |
    | |                   | |  |
    | |     EMULATOR      | |  |
    | |       =)          | |  |
    | | LIVE, HACK, GROW  | |  |
    | | ]                 | | ,|
    | !___________________! |(c|
    !_______________________!__!
    |    ___ -=      ___ -= | ,|
    | ---[_]---   ---[_]--- |(c|

    !_______________________!__!
   /                            \
  /  [][][][][][][][][][][][][]  \
 /  [][][][][][][][][][][][][][]  \
(  [][][][][____________][][][][]  )
 \ ------------------------------ /
  \______________________________/
