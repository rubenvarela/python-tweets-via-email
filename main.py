#!/usr/local/bin/python
from twython import Twython, TwythonError
import json

def send_email(string_to_send):
  #http://stackoverflow.com/a/12424439/1392131
  import smtplib

  gmail_user = "user@gmail.com"
  gmail_pwd = "password"
  FROM = gmail_user
  TO = ['someone@domain.tld'] #must be a list
  SUBJECT = "New Tweets!"
  TEXT = string_to_send

  # Prepare actual message
  message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
  """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
  try:
    #server = smtplib.SMTP(SERVER) 
    server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    #server.quit()
    server.close()
    print 'successfully sent the mail'
  except:
    print "failed to send mail"


OAUTH_TOKEN='24695635-E7kE9ADZArsYcxAri6X8yHYMLMtxHo4NjcZxCenVh'
OAUTH_TOKEN_SECRET='Uw517Eyp3uM94q7dibMwfMOBgIubJxLgrg4z2rhNyI'
APP_KEY='Qq2xtU0VUMCj9SiTNaMqOw'
APP_SECRET='nzo2KbdbdTqQOF13CSJOAn6nmBY3JqosDCRrJ1Pc'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

search_results = twitter.search(q="starbucks", count='10', geocode='18.229351,-66.456299,83mi')

tweets_to_send = "Last ten tweets matching the word 'starbucks': \r\n\r\n"

for each_tweet in search_results['statuses']:
  tweets_to_send = tweets_to_send + each_tweet['text'].encode('utf-8') + '\r\n\r\n'

send_email(tweets_to_send)