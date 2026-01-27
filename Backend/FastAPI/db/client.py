
from pymongo import MongoClient

# Establecemos la conexión con la base de datos

# Base de datos local
# db_client = MongoClient().local

# Base de datos remota
db_client = MongoClient(
    'mongodb+srv://leon3847w_db_user:kLZ6LgNZIFLVVV0A@cluster0.1h8r1ck.mongodb.net/?appName=Cluster0'
).test