from fireo import connection as firebase_connection


def initialize():
    firebase_connection(from_file="certificate.json")


def get_db():
    from fireo import db

    try:
        return db
    finally:
        db.conn.close()
