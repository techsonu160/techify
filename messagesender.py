import requests
import json

def send_sms(number,send_sms1):
    url='https://www.fast2sms.com/dev/bulk'
    params ={'authorization':'cS6qXjLao9yPmVrMkOGv8euBWzC0tQilnbZYsHd7F5E3KJ1fpRxFAd4lMrfQ2Dhv6KpU1Yi7WCjaBqwo',
            'sender_id':'FSTSMS',
            'message':mess,
            'language':'english',
            'route':'p',
            'numbers':num1

            }
    response=requests.get(url,params=params)
    dict=response.json()
    print(dict)

mess=input("enter the message")
num1=int(input('enter the number'))

send_sms(mess,num1)















