from pymongo import MongoClient
from config.index import config

db_client = MongoClient(config['MONGO_URI'])  # Connect to the MongoDB server
db_name = db_client['scada']  # Create the database
db_collection = db_name['electric-meter']  # Create the collection
