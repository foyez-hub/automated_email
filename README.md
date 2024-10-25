

# Automated Email Sender

This project automates the process of sending emails using a Python script and cron jobs. It reads email content from a text file and sends it using the specified credentials.

## Prerequisites

- Python 3.x installed on your system
- Pip (Python package manager)
- A Gmail account (or any SMTP server)
- Access to your terminal (bash)

## Setup Instructions

### 1. Clone the Repository

If you haven't done so yet, clone the repository to your local machine:

```bash
git clone https://github.com/foyez-hub/automated_email.git
cd automated_email
```

### 2. Create a Virtual Environment (Optional but Recommended)

It's a good practice to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

Create a `requirements.txt` file in your project directory with the following content:

```
python-dotenv
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Create Environment Variables

You will find an `example.env` file in the repository. This file contains a template for the environment variables you need to set up. 

#### Modify the `.env` File

1. Copy the `example.env` file to create your `.env` file:

   ```bash
   cp example.env .env
   ```

2. Open the `.env` file in a text editor and modify the following variables:

   ```plaintext
   EMAIL=example@gmail.com
   PASSWORD=your_app_specific_password_here   # Change this to your email password or app-specific password
   RECIPIENT_EMAIL=example@gmail.com  # Change this to the recipient's email address
   SUBJECT=Test Email                          # Change this to your desired email subject
   EMAIL_CONTENT_FILE=give full txt file path 
   ATTACHMENT=full path  of the attachment txt file 
   SEND_ATTACHMENT=Set it to True if you want to attach the text; otherwise, set it to False.
   ```

   - **Note**: If you are using Gmail and have two-factor authentication enabled, generate an [App Password](https://support.google.com/accounts/answer/185201) to use instead of your regular password.

### 5. Create the Email Content File

Create a text file named `email_content.txt` in the project directory. This file should contain the content you want to send in your email.

### 6. Write the Python Script

Ensure your Python script (e.g., `main.py`) is set up to read the email content and send the email using the provided credentials. Use absolute paths in your script to avoid issues with the cron job.

### 7. Create a Shell Script

Create a shell script named `send_email.sh` in the project directory:

```bash
#!/bin/bash

# Activate the virtual environment if you're using one
source /path/to/your/venv/bin/activate  # Change this to your virtual environment path

# Run the Python script
python /path/to/your/main.py  # Change this to the full path of your main.py
```

Make sure to give it execute permissions:

```bash
chmod +x send_email.sh
```

### 8. Set Up the Cron Job

Open the crontab editor:

```bash
crontab -e
```

Exmaple: Add the following line to schedule the email to be sent every day at 12:05 PM:

```bash
5 12 * * * /full/path/to/your/send_email.sh >> /full/path/to/your/logfile.log 2>&1
```

- **Change** `/full/path/to/your/` to the actual path of your script and log file.

### 9. Save and Exit

After adding the cron job, save and exit the editor. Your cron job should now be set up.

### 10. Check Logs

If you want to see logs or error messages from your script, check the `logfile.log` file:

```bash
cat /full/path/to/your/logfile.log
```

### 11. Testing

To test your setup, you can temporarily change the cron job to run every minute:

```bash
* * * * * /full/path/to/your/send_email.sh >> /full/path/to/your/logfile.log 2>&1
```

After testing, remember to revert it to your desired schedule.

## Troubleshooting

- If you encounter a "file not found" error, ensure you are using absolute paths in your script.
- If the script doesn't run, check the cron service status with `systemctl status cron` and ensure it’s active.
- Review the `logfile.log` for any error messages to diagnose issues.



