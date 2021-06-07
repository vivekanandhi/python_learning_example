import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html= Template(Path('index.html').read_text())
email = EmailMessage()
email['from']= 'vivekanandhi Rajasekaran'
email['to']= 'vivekanandhi14@gmail.com'
email['subject']= 'All is well!'

email.set_content(html.substitute({'name' :'tintin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=2525) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('vma2347@gmail.com', 'Password@1234')
    smtp.send_message(email)
    print('all good !')

