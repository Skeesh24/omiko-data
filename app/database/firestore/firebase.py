from os import environ, remove
from os.path import curdir

from fireo import connection as firebase_connection

cert = """
{
    "type": "service_account",
    "project_id": "omiko-data",
    "private_key_id": "%s",
    "private_key": "%s",
    "client_email": "%s",
    "client_id": "%s",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "%s",
    "universe_domain": "googleapis.com"
}
""" % (
    environ.get("PRIVATE_KEY_ID"),
    environ.get("PRIVATE_KEY"),
    environ.get("CLIENT_EMAIL"),
    environ.get("CLIENT_ID"),
    environ.get("CLIENT_X509_CERT_URL"),
)


def initialize():
    path = "certificate.json"
    with open(f"{curdir}/{path}", "w") as file:
        file.write(cert)
    firebase_connection(from_file=path)
    remove(path)


def get_db():
    from fireo import db

    try:
        return db
    finally:
        pass


# db init
initialize()
