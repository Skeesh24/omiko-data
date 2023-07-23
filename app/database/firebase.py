from fireo import connection as firebase_connection


def initialize():
    firebase_connection(from_file="certificate.json")
