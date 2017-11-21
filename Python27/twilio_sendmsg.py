from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC413ca882abc0ca2df066e34d84ae1b86"
# Your Auth Token from twilio.com/console
auth_token  = "b86a66fc4309707dfe2be7862aea4707"

client =    Client(account_sid, auth_token)

message = client.messages.create(
    to="+18163283353", 
    from_="+12028313914",
    body="Hello from Python!")

print(message.sid)
