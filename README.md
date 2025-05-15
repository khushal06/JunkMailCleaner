# Junk Mail Cleaner

A secure Python-based web application that connects to Gmail using App Passwords and IMAP to permanently delete all emails from a specified sender. Built with Flask and designed for users who want to remove unwanted newsletters, spam, or promotional emails from their Gmail inbox and All Mail folder.

---

## Features

- Secure Gmail login via App Password (no real password required)
- Permanently deletes emails across Inbox, All Mail, and Promotions
- Styled Flask frontend with form validation and user instructions
- Displays confirmation message and count of deleted emails
- IMAP expunge logic to bypass Gmail's archive behavior
- Ready for deployment (SSH-enabled and render-compatible)

---

## Tech Stack

- Backend: Python 3, Flask, IMAP (imaplib)
- Frontend: HTML, CSS (basic styling with Flask templates)
- Version Control: Git + GitHub (SSH)
- Deployment : Render

- ## Live Demo
Access the live app here: [https://junk-mail-cleaner.onrender.com](https://junk-mail-cleaner.onrender.com)

> Note: This free instance may take ~30 seconds to wake up if inactive.



