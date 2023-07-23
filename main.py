from fireo import connection as firebase_connection
from fireo.models import Model
from fireo.fields import TextField


firebase_connection(from_file="certificate.json")


class User(Model):
    email = TextField()
    password = TextField()


user: User = User.collection.limit(1).get()
print(user.to_dict())
