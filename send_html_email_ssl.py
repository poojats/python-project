import smtplib
from email.message import EmailMessage
from email.utils import make_msgid


def send_email():
    sender = "your_email@gmail.com"
    receiver = "receiver_email@gmail.com"
    app_password = "your_app_password"   # Gmail App Password

    # Create email object
    email_msg = EmailMessage()
    email_msg["Subject"] = "HTML message with attachments"
    email_msg["From"] = sender
    email_msg["To"] = receiver

    # Plain text fallback
    email_msg.set_content("This is a text message")

    # HTML body
    image_cid = make_msgid()
    html_body = f"""
    <html>
      <body>
        <p>Hello</p>
        <p>This email demonstrates sending an image and a PDF using Python.</p>
        <img src="cid:{image_cid[1:-1]}">
      </body>
    </html>
    """
    email_msg.add_alternative(html_body, subtype="html")

    # Attach image (inline)
    with open("sample.jpg", "rb") as image_file:
        email_msg.get_payload()[1].add_related(
            image_file.read(),
            maintype="image",
            subtype="jpeg",
            cid=image_cid
        )

    # Attach PDF
    with open("sample.pdf", "rb") as pdf_file:
        email_msg.add_attachment(
            pdf_file.read(),
            maintype="application",
            subtype="pdf",
            filename="sample.pdf"
        )

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, app_password)
        server.send_message(email_msg)

    print("Email sent successfully")


if __name__ == "__main__":
    send_email()
