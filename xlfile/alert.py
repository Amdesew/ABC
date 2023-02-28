import keys
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

client = Client(keys.account_sid, keys.account_token)

message = client.messages.create(
  body="We Are Watching You1",
  from_="+12024996272",
  to="+251929553549"
)

print(message.body)