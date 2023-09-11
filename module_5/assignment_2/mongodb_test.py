
from pymongo.mongo_client import MongoClient

url = "mongodb+srv://admin:admin>@cluster0.rspeheo.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(url)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)