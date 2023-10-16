from typing import List

from database.config import sett
from sqlalchemy import ARRAY, UUID, Column, Float, String, Table, text
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

Base = automap_base()


class Office(Base):
    __tablename__ = sett.OFFICE_TABLENAME
    id = Column(UUID(False), primary_key=True, server_default=text("gen_random_UUID()"))
    address = Column(String(100), nullable=False)
    city = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(String(11), nullable=False)


class Order(Base):
    __tablename__ = sett.ORDER_TABLENAME
    id = Column(UUID(False), primary_key=True, server_default=text("gen_random_UUID()"))
    price = Column(Float(), nullable=False)
    products = Column(ARRAY(String(36)), nullable=False)
    user = Column(String(36), nullable=False)


class Cabinet(Base):
    __tablename__ = sett.CABINET_TABLENAME
    id = Column(UUID(False), primary_key=True, server_default=text("gen_random_UUID()"))
    cart = Column(ARRAY(String(36)), nullable=False)
    city = Column(String(20), nullable=False)
    favourites = Column(ARRAY(String(36)), nullable=False)
    orders = Column(ARRAY(String(36)), nullable=False)
    phone = Column(String(11), nullable=False)


class Product(Base):
    __tablename__ = sett.PRODUCT_TABLENAME
    id = Column(UUID(False), primary_key=True, server_default=text("gen_random_UUID()"))
    description = Column(String(100), nullable=False)
    name = Column(String(30), nullable=False)
    price = Column(Float(), nullable=False)
    short_description = Column(String(30), nullable=False)
    category = Column(String(30), nullable=False)


class Product_Category(Base):
    __tablename__ = sett.PRODUCT_CATEGORY_TABLENAME
    id = Column(UUID(False), primary_key=True, server_default=text("gen_random_UUID()"))
    name = Column(String(30), nullable=False)
    product_count = Column(Float(), nullable=False)
