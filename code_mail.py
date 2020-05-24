import smtplib
import urllib.request as urllib
# Senders email
sender_email = "sumeetsumit8@gmail.com"
# Receivers email
rec_email = "sumeetsumit8@gmail.com"

message = "Best Modelcreated..."
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("sumeetsumit8@gmail", "Password")
print("Login Success!")
# Send Email
server.sendmail("Sumeet Gairola", "sumeetsumit8@gmail", message)