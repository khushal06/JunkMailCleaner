import imaplib

def delete_emails(email_user, email_pass, sender_email):
    try:
        # Ensure all strings are encoded safely
        email_user = email_user.encode("utf-8").decode("utf-8").strip()
        email_pass = email_pass.encode("utf-8").decode("utf-8").strip()
        sender_email = sender_email.encode("utf-8").decode("utf-8").strip()

        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(email_user, email_pass)
        imap.select('"[Gmail]/All Mail"')

        status, messages = imap.search(None, f'FROM "{sender_email}"')
        email_ids = messages[0].split()

        if not email_ids:
            return f"No emails found from {sender_email}."

        for eid in email_ids:
            imap.store(eid, "+FLAGS", "\\Deleted")

        imap.expunge()
        imap.logout()
        return f"✅ Deleted {len(email_ids)} emails from {sender_email}."
    except Exception as e:
        return f"❌ Error: {str(e)}"
