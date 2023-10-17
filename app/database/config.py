from dataclasses import dataclass
from os import environ


@dataclass
class sett:
    PROVIDER: str = environ.get("PROVIDER")
    DRIVER: str = environ.get("DRIVER")
    DB_USER: str = environ.get("DB_USER")
    DB_PASSWORD: str = environ.get("DB_PASSWORD")
    DB_HOST: str = environ.get("DB_HOST")
    DB_PORT: str = environ.get("DB_PORT")
    DB_DBNAME: str = environ.get("DB_DBNAME")
    OFFICE_TABLENAME: str = environ.get("OFFICE_TABLENAME")
    PRODUCT_TABLENAME: str = environ.get("PRODUCT_TABLENAME")
    ORDER_TABLENAME: str = environ.get("ORDER_TABLENAME")
    CABINET_TABLENAME: str = environ.get("CABINET_TABLENAME")
    PRODUCT_CATEGORY_TABLENAME: str = environ.get("PRODUCT_CATEGORY_TABLENAME")
