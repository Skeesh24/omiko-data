from app.database.entities import (
    Cabinet,
    Office,
    Order,
    Product,
    ProductCategory,
    User,
)
from app.models.repositories.repository import FirebaseRepository


def get_user_repository():
    repo = FirebaseRepository[User]()

    try:
        return repo
    finally:
        pass


class UoW:
    product = FirebaseRepository[Product]()
    order = FirebaseRepository[Order]()
    product_category = FirebaseRepository[ProductCategory]()
    office = FirebaseRepository[Office]()
    cabinet = FirebaseRepository[Cabinet]()
    ...


def get_uow():
    return UoW()
