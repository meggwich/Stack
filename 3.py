import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailClient:
    def __init__(self, login, password, smtp_server="smtp.gmail.com", imap_server="imap.gmail.com"):
        self.login = login
        self.password = password
        self.smtp_server = smtp_server
        self.imap_server = imap_server

    def send_mail(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.smtp_server, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, msg.as_string())
        ms.quit()

    def receive_mail(self, header=None):
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message

if __name__ == '__main__':
    client = MailClient('login@gmail.com', 'qwerty')
    client.send_mail(['vasya@email.com', 'petya@email.com'], 'Subject', 'Message')
    client.receive_mail()

