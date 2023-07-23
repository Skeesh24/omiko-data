from fireo import connection as firebase_connection
from models import User


firebase_connection(from_file="certificate.json")


user: User = User.collection.limit(1).get()
print(user.to_dict())
