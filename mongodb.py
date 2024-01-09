from pymongo import MongoClient

# Set up MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["assistant_db"]
collection = db["conversations"]

def store_in_mongodb(user_input, assistant_response):
    data = {
        "user_input": user_input,
        "assistant_response": assistant_response,
    }
    collection.insert_one(data)

