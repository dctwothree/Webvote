import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "ragiosta@gmail.com"
pas = "Gibson@Fender23"

sms_gateway = '4012300510@pm.sprint.com'
# The server we use to send emails in our case it will be gmail but every email provider has a different smtp
# and port is also provided by the email provider.
smtp = "smtp.gmail.com"
port = 587
# This will start our email server
server = smtplib.SMTP('smtp.gmail.com', 587)
# Starting the server
server.ehlo()

server.starttls()


# Now we need to login
server.login('ragiosta@gmail.com', "Gibson@Fender23")

# Now we use the MIME module to structure our message.
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sms_gateway
# Make sure you add a new line in the subject
msg['Subject'] = "The voting has closed\n"
# Make sure you also add new lines to your body
body = "Fuck everyone\n"
# and then attach that body furthermore you can also send html content.
msg.attach(MIMEText(body, 'plain'))

sms = msg.as_string()

server.sendmail(email,sms_gateway,sms)

# lastly quit the server
server.quit()