# Import the necessary libraries
from pymongo import MongoClient

# Connect to the MongoDB server running locally
client = MongoClient("localhost", 27017)

# Access the database
db = client."410-305O.db"

# Access the collection named 'students'
students = db.students

# Display all documents in the collection
print("All Documents in the Collection:")
for student in students.find({}):
    print(student)

# Display a single document by student_id (replace with the desired student_id)
desired_student_id = 1007
student = students.find_one({"student_id": desired_student_id})

if student:
    print(f"Student with student_id {desired_student_id}:")
    print(student)
else:
    print(f"No student found with student_id {desired_student_id}")

# Close the MongoDB connection
client.close()
