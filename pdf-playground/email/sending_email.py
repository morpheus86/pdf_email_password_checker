import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Tidiane"
email["to"] = "the email you want to send it to"
email["subject"] = "You recently won a bunch of money"

email.set_content("I am a Python Programmer")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # creating server
    smtp.starttls()  # encryption mechanism
    smtp.login("useremail", "password")  # login in to the gmail account pass credential
    smtp.send_message(email)
    print("all good email")
