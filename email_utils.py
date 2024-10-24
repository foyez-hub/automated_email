import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Function to read email content from a .txt file
def read_email_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to send the email
def send_email(sender_email, sender_password, recipient_email, subject, content):
    try:
        # Create a MIMEMultipart object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email content
        msg.attach(MIMEText(content, 'plain'))

        # Set up the SMTP server (using Gmail's SMTP server)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login to the email account
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        
        print("Email sent successfully!")
    
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
