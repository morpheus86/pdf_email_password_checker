import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # similar to the os module

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Tidiane"
email["to"] = "email"
email["subject"] = "Html email through Python"

email.set_content(html.substitute(name="Tidiane"), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email address", "Password")
    smtp.send_message(email)
    print("all work perfectly")