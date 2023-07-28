from app.database.entities import Office, Order, Product, Product_Category, User
from app.models.repositories.repository import FirebaseRepository


def get_user_repository():
    repo = FirebaseRepository[User]()

    try:
        return repo
    finally:
        pass


def get_product_repository():
    repo = FirebaseRepository[Product]()

    try:
        return repo
    finally:
        pass


def get_order_repository():
    repo = FirebaseRepository[Order]()

    try:
        return repo
    finally:
        pass


def get_product_category_repository():
    repo = FirebaseRepository[Product_Category]()

    try:
        return repo
    finally:
        pass


def get_office_repository():
    repo = FirebaseRepository[Office]()

    try:
        return repo
    finally:
        pass


def get_cabinet_repository():
    repo = FirebaseRepository[Office]()

    try:
        return repo
    finally:
        pass
