from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGO_URI)
db = client["chatgpt_clone"]
users_collection = db["users"]
