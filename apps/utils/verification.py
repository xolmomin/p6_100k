from random import randint

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from root.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_VERIFY_SERVICE_SID

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
verify = client.verify.services(TWILIO_VERIFY_SERVICE_SID)


def send(phone, fake=False):
    if fake:
        print(randint(11111, 99999))
        return
    verify.verifications.create(to=phone, channel='sms')


def check(phone, code, fake=False):
    if fake:
        return True
    try:
        result = verify.verification_checks.create(to=phone, code=code)
    except TwilioRestException:
        print('no')
        return False
    return result.status == 'approved'
