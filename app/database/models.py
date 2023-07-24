from fireo.models import Model
from fireo.fields import TextField, NumberField, ListField


class User(Model):
    email = TextField()
    password = TextField()


class Product(Model):
    name = TextField()
    short_description = TextField()
    description = TextField()
    category = TextField()
    price = NumberField()


class Product_Category(Model):
    name = TextField()
    product_count = NumberField()


class Office(Model):
    city = TextField()
    address = TextField()
    phone = TextField()
    email = TextField()


class Cabinet(Model):
    cart = ListField(nested_field=TextField)
    favourites = ListField(nested_field=TextField)
    orders = ListField(nested_field=TextField)
    city = TextField()
    phone = TextField()


class Order(Model):
    user = TextField()
    products = ListField(nested_field=TextField)
    price = NumberField()
