import email
import imaplib
import os

user = 'gerardkodjo9@gmail.com'
password = 'efua02605790'
imap_url = 'imap.gmail.com'
"""
# Pas trop important
# cette variable appartient a celui .......
attachement_dir = 'C:/Users/Administrateur/Desktop/testCodeAttach/test/'
"""

def authUser(user, password, imap_url):
    con = imaplib.IMAP4_SSL(imap_url, 993)
    con.login(user, password)
    return con

"""
# ....appartient a celui la
# cette fonction permet de telecharger tous les email dans un dossier dont tu peux specifié
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


"""
""" 
# cette fonction permet de recuperer le message d'email a partir de son index 
"""
def getbody(msgs):
    # si le message a recuperer est de fonction ou de  type multipart
    # alors on le recupere sous forme de " b'message' "
    if msgs.is_multipart():
        return getbody(msgs.get_payload(0))
    else:
        # au cas contraire le chargement du message est inexistant
        return msgs.get_payload(None, True)

    
    """ 
    cette fonction permet de recuperer le result de la recherche sur l'index renseigner, etant connecter
    # key: index
    # value: le message a affiché
    # con: la connexion te permettant d'acceder au mail renseigner
    """
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

# ici la fonction permet d'obtenir les grands tittre du compte email
# et recuperrer le tittre voulu aek sa reference pour l'idenfier 
# RFC822 est la reference de l'inbox
# et cette fonction recupere le message de l'email sous forme de bit
def get_emails(result_bytes):
    """
    # le tableau msg declare permet d'ajouter tous les donnée recuperer dans le tableau msgs
    # et return le messgae demander
    """
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
        return msgs


con = authUser(user, password, imap_url)
con.select('INBOX')

result, data = con.fetch(b'51', '(RFC822)')
raw = email.message_from_bytes(data[0][1])
# get_attachement(raw)
print(getbody(raw))
print("/************ PRINT SECOND*************/")
print(getbody(email.message_from_bytes(data[0][1])))
