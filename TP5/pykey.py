import sys, io, os, string
import secrets, base64
from getpass import getpass
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

punct = ".:!?/()&#@&_-*%"
keychain_path = "keychain.dat"
delimiter = "§"
salt = b'\x05S\xa9\xdcQ\x00\xe4\xbe\x1f\x82\xe1Ii\x04\xe4h'



def load_passwords(key):
    if not os.path.isfile(keychain_path):
        save_passwords({}, key)

    with open(keychain_path, 'rb') as f:
        data = f.read()

    # Déchiffrement des données (avec gestion de l'exception si le mot de passe est erroné)
    fernet = Fernet(key)
    try:
        data = fernet.decrypt(data)
    except InvalidToken:
        print("Wrong master password.")
        sys.exit()
    
    data = data.decode()

    db = {}
    for l in io.StringIO(data):
        l = l.strip()
        if l:
            s = l.split(delimiter)
            if len(s) == 2:
                db[s[0]] = s[1]
    return db


def save_passwords(db, key):
    data = "\n".join(w + delimiter + p for w, p in db.items())
    data = data.encode()

    fernet = Fernet(key)
    data = fernet.encrypt(data)

    with open(keychain_path, 'wb') as f:
        f.write(data)


def is_strong_enough(password):
    return (any(s.isupper() for s in password))\
        and (any(s.islower() for s in password))\
        and (any(s.isdigit() for s in password))\
        and (s in punct for s in password)


def generate_password(size=13):
    alphabet = punct + string.ascii_lowercase + string.ascii_uppercase + string.digits
    while True:
        pwd = "".join(secrets.choice(alphabet) for _ in range(size))
        if is_strong_enough(pwd):
            return pwd

def generate_key(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def get_password(db, name):
    if name in db:
        print(db[name])
    else:
        print(db.keys())
    return


def set_password(db, name):
    new_pwd = generate_password()
    db[name] = new_pwd
    # print(new_pwd)
    print(f'Nouveau mot de passe pour "{name}" : {new_pwd}') # esthétique
    return


def print_help():
    print("Usage :")
    print('- "python pykey.py get name" to get the password associated to site "name"')
    print('- "python pykey.py set name" to generate (and replace) the password associated to site "name"')
    sys.exit()


def main():
    print("Pykey - Password manager")

    if len(sys.argv) <= 1:
        print_help()
    elif sys.argv[1] == "get" and len(sys.argv) == 3:
        action = get_password
    elif sys.argv[1] == "set" and len(sys.argv) == 3:
        action = set_password
    else:
        print_help()

    # Saisie sécurisée du mot de passe maître et génération de la clé correspondante
    master_password = getpass("Enter your master password: ")
    key = generate_key(master_password)
    #key = b'WNlS4K1hLhAVl8JiYV0Fj8e92EiSEQi5VS4KNGNPQCc='

    db = load_passwords(key)
    action(db, sys.argv[2])
    save_passwords(db, key)

if __name__ == "__main__":
    main()