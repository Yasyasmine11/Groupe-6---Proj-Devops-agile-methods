# Alerte email

import smtplib

def send_email(subject, body, to_email):
    msg = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your_email", "your_password")
        server.sendmail("your_email", to_email, msg)
