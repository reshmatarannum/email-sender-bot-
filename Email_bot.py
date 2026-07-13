import smtplib
import ssl
import getpass

sender_email = input("Sender email: ").strip()
receiver_email = input("Receiver email: ").strip()
password = input("Password or App Password of sender email: ")

subject = input("Subject: ").strip()
body = input("Body: ")

if not sender_email or not receiver_email or not password:
    print("Sender email, receiver email, and password are required.")
    exit(1)

message = f"Subject: {subject}\n\n{body}"
context = ssl.create_default_context()
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print("Failed to send email: authentication failed.")
    print("Please verify your sender email, app password, and Gmail account security settings.")
    print("SMTPAuthenticationError:", e)
except Exception as e:
    print("Failed to send email:", type(e)._name_, e)
    print("If you are using Gmail, make sure App Password is enabled and you used the full Gmail address.")