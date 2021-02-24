import gspread
import schedule
import smtplib
import os


#Send and email using smtplib through gmail
def send_alert(recipient, subject, msg):
    
    #sets up access to mailserver base on the user info located in .zshrc or whatever the defaul shell is
    email_username = os.environ.get('email_username')
    email_password = os.environ.get('email_python_password')
    
    server = smtplib.SMTP('smtp.gmail.com')
    server.connect('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.login(email_username, email_password)
  
    #  formats the email to be sent properly by .sendmail
    email = f'Subject: {subject}\n\n{msg}'

    server.sendmail(email_username, recipient, email)

send_alert('2626234965@email.uscc.net', 'Record Your Calories', 'Do it, or I\'ll murder you')        