
from pymongo.mongo_client import MongoClient

url = "mongodb+srv://admin:admin@cluster0.rspeheo.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(url)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

    
# Connect pytech database
db = client.pytech

# Fetch students collection 
students = db.students

# Find 'students' in collection 
student_list = students.find({})

# Display required message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# Loop collection and output results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Update student id 1007, Yugi Mutou
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Mutou"}})

# find the updated student document 
Yugi = students.find_one({"student_id": "1007"})

# Display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# Output updated document to the terminal window
print("  Student ID: " + Yugi["student_id"] + "\n  First Name: " + Yugi["first_name"] + "\n  Last Name: " + Yugi["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")