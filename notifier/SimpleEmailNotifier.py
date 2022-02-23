import smtplib
from email.mime.text import MIMEText

class SimpleEmailNotifier:


    def send(self):
        try:
            msg = MIMEText("Test 123")

            # me == the sender's email address
            # you == the recipient's email address
            msg['Subject'] = "Test Email"
            msg['From'] = "test@test"
            msg['To'] = "marionmaiden@gmail.com"

            # Send the message via our own SMTP server.
            s = smtplib.SMTP('localhost')
            s.send_message(msg)
            s.quit()
        except:
            print("aqui")