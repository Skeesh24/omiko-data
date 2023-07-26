from app.database.entities import (
    User,
    Cabinet,
    Office,
    Product_Category,
    Product,
    Order,
)


def type_asscociation(object) -> str:
    if isinstance(object, User):
        return "user"
    if isinstance(object, Office):
        return "office"
    if isinstance(object, Product_Category):
        return "product_category"
    if isinstance(object, Product):
        return "product"
    if isinstance(object, Order):
        return "order"
    if isinstance(object, Cabinet):
        return "cabinet"
