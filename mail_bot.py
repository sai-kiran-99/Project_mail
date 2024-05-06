
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Function to compose an email
def compose_email(sender, receiver, subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file
    filename = attachment_path.split('/')[-1]
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
    msg.attach(part)

    return msg

# Function to send an email
def send_email(sender_email, receiver_email, password, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {receiver_email}!")
    except Exception as e:
        print(f"Error: {e}")

# Email credentials
SENDER_EMAIL = ''
SENDER_PASSWORD = ''  # Replace with your actual sender password

# Read receiver emails from the CSV file
def read_receiver_emails(file_path):
    receiver_emails = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            receiver_emails.extend(row)
    return receiver_emails

# Provide email details
SUBJECT = 'Poster'
BODY = """My hotel"""

ATTACHMENT_PATH = r''  # Corrected path

# Read receiver emails from CSV file
file_path = r''  # Corrected path
receiver_emails = read_receiver_emails(file_path)

# Loop through each receiver email and send an email
for receiver_email in receiver_emails:
    # Compose email message
    email = compose_email(SENDER_EMAIL, receiver_email, SUBJECT, BODY, ATTACHMENT_PATH)
    # Send email
    send_email(SENDER_EMAIL, receiver_email, SENDER_PASSWORD, email)



