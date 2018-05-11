import imaplib #imports imap package 
import json
mail = imaplib.IMAP4_SSL('imap.gmail.com') #imap url
mail.login('', '') #email info

