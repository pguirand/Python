import email_config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# configuration below imported from email_config
'''config_email = "papoche25@gmail.com"
config_password = "plkwpkavdsifehjq"
config_server = "smtp.gmail.com"
config_server_port = 587'''

def send_mail(recipient, sujet, message):

    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = sujet
    multipart_message["From"] = email_config.config_email
    multipart_message["To"] = recipient
    multipart_message.attach(MIMEText(message, "plain")) # or html for plain

    serveur_mail = smtplib.SMTP(email_config.config_server, email_config.config_server_port)
    serveur_mail.starttls()
    serveur_mail.login(email_config.config_email, email_config.config_password)
    serveur_mail.sendmail(email_config.config_email, recipient, multipart_message.as_string())
    multipart_message.as_string()
    serveur_mail.quit()

contenu_mail = """ Bonjour, 

Ceci est un test d'automatisation d'envoie de mail.
Merci de confirmer la reception.
Bien a vous, 
Pipo
"""

# send_mail("papoche25@gmail.com", contenu_mail)
send_mail("p_guirand@hotmail.com", "Test Mail", contenu_mail)


