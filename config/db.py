from pymongo import MongoClient

MONGO_URI  = "mongodb+srv://notzzuser:Rishi005@cluster0.8mj5vdj.mongodb.net/"

conn = MongoClient(MONGO_URI)
def get_user_collection():
    return conn["users"]