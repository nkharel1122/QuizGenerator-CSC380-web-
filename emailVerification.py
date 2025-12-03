import os
import requests

RESEND_API_KEY = os.getenv("RESEND_API_KEY")


def sendMessage(address, code: str) -> None:

    if not RESEND_API_KEY:
        raise RuntimeError("RESEND_API_KEY is not set in environment variables.")

    payload = {
        "from": "QuizBot <onboarding@resend.dev>", 
        "to": [address],
        "subject": "Verification Code",
        "text": f"{code} is your verification code. If this was not you, ignore this email.",
    }

    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=10,
    )

    if response.status_code >= 400:
        raise RuntimeError(f"Resend error {response.status_code}: {response.text}")
