1. Confirm you are using a Gmail account

Must be @gmail.com or Google Workspace

NOT Outlook / Yahoo / company SMTP

2. 2-Step Verification MUST be ON

Go to:
👉 https://myaccount.google.com/security

Check:

✅ “2-Step Verification” → ON

⚠️ Without this, App Passwords will not work

3. Create a NEW App Password (don’t reuse old)

Go to:
👉 https://myaccount.google.com/apppasswords

Select:

App: Mail

Device: Windows Computer

Click Generate

You will get something like:

abcd efgh ijkl mnop


✔ Copy it
✔ REMOVE spaces when pasting

4. Your login line MUST look like this
fromEmail = "your_email@gmail.com"

s.login(fromEmail, "abcdefghijklmnop")  # 16 chars, no spaces