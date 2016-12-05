# Import the twilio python library
from twilio.rest import TwilioRestClient

account_sid = "AC83a335c4121dd2929c5b1174b3be58f1"
auth_token = "f54ba175ffc77b92d87cc2a55e637e7c"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to = "+14157128968", from_ = "+12242314074", body = "Let's do this!")
