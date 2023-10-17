from database.mysql.entities import (
    Cabinet,
    Office,
    Order,
    Product,
    Product_Category,
)
from database.firestore.repository import FirebaseRepository
from database.mysql.repository import MysqlRepository


class FirestoreUoW:
    # product = FirebaseRepository[Product]()
    # order = FirebaseRepository[Order]()
    # product_category = FirebaseRepository[ProductCategory]()
    # office = FirebaseRepository[Office]()
    # cabinet = FirebaseRepository[Cabinet]()
    ...


class MysqlUoW:
    product = MysqlRepository(Product)
    order = MysqlRepository(Order)
    product_category = MysqlRepository(Product_Category)
    office = MysqlRepository(Office)
    cabinet = MysqlRepository(Cabinet)


def get_uow():
    return MysqlUoW()
