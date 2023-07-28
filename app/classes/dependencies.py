from app.database.entities import Order, Product, User
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


