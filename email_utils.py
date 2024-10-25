import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders
import os


def read_email_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def send_email(sender_email, sender_password, recipient_email, subject, content, attachment_path=None):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(content, 'plain'))

        if attachment_path and os.path.isfile(attachment_path):
            with open(attachment_path, 'rb') as attachment_file:
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(attachment_file.read())
                
                encoders.encode_base64(attachment)
                
                attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
                
                msg.attach(attachment)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        server.login(sender_email, sender_password)
        
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        
        print("Email sent successfully with attachment!" if attachment_path else "Email sent successfully!")
    
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
