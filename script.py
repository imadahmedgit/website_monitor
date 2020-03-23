import os
import smtplib
import requests
import logging

EMAIL_ADDRESS=os.environ.get('EMAIL_USER')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')

def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'YOUR SITE IS DOWN!'
        body = 'Make sure the server restarted and it is back up'
        msg = f'Subject: {subject}\n\n{body}'

        logging.info('Sending Email...')
        smtp.sendmail(EMAIL_ADDRESS, 'emtiaz.aiub17@gmail.com', msg)


try:
    r = requests.get('https://google.com', timeout=5)
    print(EMAIL_ADDRESS)
    print(EMAIL_PASSWORD)
    if r.status_code != 200:
        logging.info('Website is DOWN!')
        notify_user()
    else:
        logging.info('Website is UP')
        notify_user()

except Exception as e:
    logging.info('Website is DOWN!')
    notify_user()