import os
import smtplib
from email.mime.text import MIMEText
from threading import Thread

EMAIL_ADDR = "quizbotverifier@gmail.com"
EMAIL_PASS = os.environ.get("EMAIL_PASS")


def _send_email(address, code):
    body = f"{code} is your verification code. If this was not you, ignore this email."
    msg = MIMEText(body, "plain")
    msg["Subject"] = "Verification Code"
    msg["From"] = EMAIL_ADDR
    msg["To"] = address

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as server:
            server.starttls()
            server.login(EMAIL_ADDR, EMAIL_PASS)
            server.sendmail(EMAIL_ADDR, [address], msg.as_string())
        print(f"Sent verification email to {address}")
    except Exception as e:
        print(f"Email send error: {e}")


def sendMessage(address, code):
    if not address.lower().endswith("@oswego.edu"):
        raise ValueError("Email must be an @oswego.edu address.")
    Thread(target=_send_email, args=(address, code), daemon=True).start()