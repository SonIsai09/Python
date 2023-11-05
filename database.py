from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://2512242023:Isai091995@cluster0.yltg9md.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():

    try:
         client = MongoClient(MONGO_URI, tlsCAFile=ca)
         db = client["dbb_planillas_app"]
    except ConnectionError:
          print('Error de conexión con la Base')
    return db

        
    
