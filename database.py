from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://username:4vuUw2ccpC92O1lZ@cluster0.ipz2yn2.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()


def db_connection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_players_app"]
        return db
    except ConnectionError as e:
        print('Error connecting to the DB')
        raise e
