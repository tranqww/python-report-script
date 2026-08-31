# отправка письма с вложением (smtplib)
import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_report(recipient, attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "HN Stories Report"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient
    msg.set_content("Attached is the latest report.")

    with open(attachment_path, "rb") as file:
        file_data = file.read()
        file_name = os.path.basename(attachment_path)

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=file_name,
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
            raise ValueError("EMAIL_ADDRESS or EMAIL_PASSWORD is not set")
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)