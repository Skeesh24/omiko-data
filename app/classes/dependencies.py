from app.database.entities import Product, User
from app.models.repositories.repository import FirebaseRepository
from app.database.firebase import get_db


def get_product_repository():
    repo = FirebaseRepository[Product]()

    try:
        return repo
    finally:
        pass

def get_user_repository():
    repo = FirebaseRepository[User]()

    try:
        return repo
    finally:
        pass
