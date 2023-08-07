from fireo import connection as firebase_connection
from os.path import curdir
from os import environ


def get_credentials_object():
    return {
        "type": "service_account",
        "project_id": "omiko-data",
        "private_key_id": environ.get("PRIVATE_KEY_ID"),
        "private_key": environ.get("PRIVATE_KEY"),
        "client_email": environ.get("CLIENT_EMAIL"),
        "client_id": environ.get("CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": environ.get("CLIENT_X509_CERT_URL"),
        "universe_domain": "googleapis.com",
    }


def initialize():
    creds = get_credentials_object()
    firebase_connection(credentials=creds)


def get_db():
    from fireo import db

    try:
        return db
    finally:
        pass
