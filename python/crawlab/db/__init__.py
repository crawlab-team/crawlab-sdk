import os
from pymongo import MongoClient

MONGO_HOST = os.environ.get('CRAWLAB_MONGO_HOST') or 'localhost'
MONGO_PORT = int(os.environ.get('CRAWLAB_MONGO_PORT')) or 27017
MONGO_DB = os.environ.get('CRAWLAB_MONGO_DB')
MONGO_USERNAME = os.environ.get('CRAWLAB_MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('CRAWLAB_MONGO_PASSWORD')
MONGO_AUTHSOURCE = os.environ.get('CRAWLAB_MONGO_AUTHSOURCE')
COLLECTION = os.environ.get('CRAWLAB_COLLECTION')

mongo = MongoClient(
    host=MONGO_HOST,
    port=MONGO_PORT,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    authSource=MONGO_AUTHSOURCE,
)
db = mongo.get_database(MONGO_DB)
col = db.get_collection(COLLECTION)
