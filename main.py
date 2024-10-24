from email_utils import read_email_content, send_email
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

if __name__ == '__main__':
    sender_email = os.getenv('EMAIL')
    sender_password = os.getenv('PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')  
    subject = os.getenv('SUBJECT') 
    email_content_file = os.getenv('EMAIL_CONTENT_FILE') 

    try:
        email_content = read_email_content(email_content_file)  
    except FileNotFoundError:
        print(f"Error: The file '{email_content_file}' was not found.")
        exit(1)

    try:
        send_email(sender_email, sender_password, recipient_email, subject, email_content)
        # Get the current date and time when the email is sent
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Email sent successfully (main) at {current_time}.")
    except Exception as e:
        print(f"Failed to send email. Error(main): {e}")
