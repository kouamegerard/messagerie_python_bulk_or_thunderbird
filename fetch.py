import email
import imaplib
import os

user = 'gerardkodjo9@gmail.com'
password = 'efua02605790'
imap_url = 'imap.gmail.com'
attachement_dir = 'C:/Users/Administrateur/Desktop/testCodeAttach/test/'

def authUser(user, password, imap_url):
    con = imaplib.IMAP4_SSL(imap_url, 993)
    con.login(user, password)
    return con

def get_attachement(msg):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachement_dir, fileName)
            with open(filePath, 'wb') as f:
                f.write(part.get_payload(decode=True))

def getbody(msgs):
    if msgs.is_multipart():
        return getbody(msgs.get_payload(0))
    else:
        return msgs.get_payload(None, True)

def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
        return msgs


con = authUser(user, password, imap_url)
con.select('INBOX')

result, data = con.fetch(b'51', '(RFC822)')
raw = email.message_from_bytes(data[0][1])
get_attachement(raw)
print(getbody(raw))
print("/************ PRINT SECOND*************/")
print(getbody(email.message_from_bytes(data[0][1])))