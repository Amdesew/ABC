import smtplib

sender = "amdesewseifu7@gmail.com"
reciever = "frankamde77@gmail.com"
password = "pdghzbayyxokfdek"
subject = "Python Email Test"
body = "I Wrote an email :D"

message = f"""From:{sender}
TO: {reciever}
Subject: {subject}\n
{body}"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged In")
    server.sendmail(sender, reciever, message)
    print("Email Has Been Sent!")

except smtplib.SMTPAuthenticationError:
    print("Unable To Log In")