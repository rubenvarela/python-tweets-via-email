# Send Tweets via Email

Yesterday (2013-08-15) at the prPIG meeting someone asked if you could search
Twitter and send the results via email. This is a really simple example on 
how to do that.

## Dependencies
You need to install Twython. 
You should be able to simply run `pip install twython`


## Instructions
You need to make some changes. 
 1. Where it says *gmail_user = "user@gmail.com"* , replace **user**with your Gmail username. If you're using Google Apps, replace the gmail part too in order to match your domain.
 2. Where it says *gmail_pwd = "password"*, replace **password** with your actual Gmail or Google Apps password.
 3. Where it says *TO = ['someone@domain.tld'] #must be a list*, replace **someone@domain.tld** with the email of who you want to send the email to.
