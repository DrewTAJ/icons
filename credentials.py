credentials = {
    "email": "", #Your email
    "password": "" #Your password
}

flask_secret = '' #Your secret, set it to random byts

def getCredentials():
    return credentials

def getSecret():
    return flask_secret