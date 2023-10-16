from database.config import sett
from database.mysql.entities import Base
from sqlalchemy import MetaData, create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    f"{sett.PROVIDER}+{sett.DRIVER}://{sett.DB_USER}:{sett.DB_PASSWORD}@{sett.DB_HOST}:{sett.DB_PORT}/{sett.DB_DBNAME}"
)

metadata = MetaData()
metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Base.prepare(engine, reflect=True)
session = Session()


def get_session():
    return session
