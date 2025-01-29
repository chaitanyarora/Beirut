from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

# MongoDB Connection
MONGO_URL = os.getenv('MONGO_URL')
client = MongoClient(MONGO_URL)
db = client.crud_app
collection = db.items

# MongoDB Helper Functions
def serialize_doc(doc):
    """Serialize MongoDB document to JSON-compatible format."""
    return {**doc, "_id": str(doc["_id"])}

def get_item(item_id):
    """Get a single item by ID."""
    return collection.find_one({"_id": ObjectId(item_id)})

def get_all_items():
    """Get all items."""
    return [serialize_doc(item) for item in collection.find()]

def create_item(item_data):
    """Create a new item."""
    return collection.insert_one(item_data)

def update_item(item_id, updated_data):
    """Update an existing item."""
    return collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_data})

def delete_item(item_id):
    """Delete an item."""
    return collection.delete_one({"_id": ObjectId(item_id)})
