# This file should be responsible for sending notifications with the deal flight data. Perhaps it should be a class?
from twilio.rest import Client
import os
import dotenv
import requests
from datetime import datetime, timedelta
from pprint import pprint
import smtplib

dotenv.load_dotenv()

class notication:

    def __init__(self):
        self.twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
        self.my_phone_number = os.getenv("MY_PHONE_NUMBER")

    def send_sms(self, message):
        client = Client(self.twilio_sid, self.twilio_auth_token)
        message = client.messages.create(
            body=message,
            from_=self.twilio_phone_number,
            to=self.my_phone_number
        )
        print(message.status)
