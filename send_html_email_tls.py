import smtplib
from email.message import EmailMessage
from email.utils import make_msgid

FROM_EMAIL = "your_email@gmail.com"
TO_EMAIL = "receiver_email@gmail.com"
APP_PASSWORD = "your_16_char_app_password"  # Gmail App Password

# Create email
msg = EmailMessage()
msg["Subject"] = "HTML email with attachments (SSL)"
msg["From"] = FROM_EMAIL
msg["To"] = TO_EMAIL
msg.set_content("This is a text message")

# HTML content
image_cid = make_msgid()
msg.add_alternative(f"""
<html>
  <body>
    <p>Hello</p>
    <p>This email is sent using SSL.</p>
    <img src="cid:{image_cid[1:-1]}">
  </body>
</html>
""", subtype="html")

# Attach inline image
with open("sample.jpg", "rb") as img:
    msg.get_payload()[1].add_related(
        img.read(),
        maintype="image",
        subtype="jpeg",
        cid=image_cid
    )

# Attach PDF
with open("sample.pdf", "rb") as pdf:
    msg.add_attachment(
        pdf.read(),
        maintype="application",
        subtype="pdf",
        filename="sample.pdf"
    )

# Send email (SSL)
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(FROM_EMAIL, APP_PASSWORD)
    server.send_message(msg)

print("Email sent successfully using SSL ✅")
