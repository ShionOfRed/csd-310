# Import the necessary libraries
from pymongo import MongoClient

# Connect to the MongoDB server running locally
client = MongoClient("localhost", 27017)

# Access the database
db = client."410-305O.db"

# Access the collection named 'students'
students = db.students

# Define three student documents with the specified fields
student1 = {
    "student_id": 1007,
    "first_name": "Yugi",
    "last_name": "Mutou",
    "major": "Cybersecurity"
}

student2 = {
    "student_id": 1008,
    "first_name": "Bakura",
    "last_name": "Ryou",
    "major": "Cybersecurity"
}

student3 = {
    "student_id": 1009,
    "first_name": "Marik",
    "last_name": "Ishtar",
    "major": "Cybersecurity"
}

# Insert the student documents and get the inserted_ids
new_student_id1 = students.insert_one(student1).inserted_id
new_student_id2 = students.insert_one(student2).inserted_id
new_student_id3 = students.insert_one(student3).inserted_id

# Display the returned student_ids
print("Inserted Student IDs:")
print(new_student_id1)
print(new_student_id2)
print(new_student_id3)

# Close the MongoDB connection
client.close()
