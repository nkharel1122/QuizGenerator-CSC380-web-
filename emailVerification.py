import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL", "quizbotverifier@gmail.com")


def sendMessage(address, code):
    if not SENDGRID_API_KEY:
        raise RuntimeError("SENDGRID_API_KEY is not set")

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=address,
        subject="Verification Code",
        plain_text_content=f"{code} is your verification code. If this was not you, ignore this email.",
    )

    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)

    if response.status_code >= 400:
        raise RuntimeError(f"SendGrid error {response.status_code}: {response.body}")
