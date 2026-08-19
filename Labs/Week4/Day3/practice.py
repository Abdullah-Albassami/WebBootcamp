# Guided Practice

from pathlib import Path 
import json

class InvalidStudentError(Exception):
    pass

path = Path("data") / "students.json"
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

path = data_dir / "students.json"

students = [
    {"name": "Sara", "score": 90},
    {"name": "Omar", "score": 93}
]

with path.open("w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)

try:
    with path.open("r", encoding="utf-8") as file:
        loaded_students = json.load(file)

    for student in loaded_students:
        if "name" not in student:
            raise InvalidStudentError("Student is missing a name")

        if "score" not in student:
            raise InvalidStudentError("Student is missing a score")

        if not student["name"]:
            raise InvalidStudentError("Student name cannot be empty")

        if not 0 <= student["score"] <= 100:
            raise InvalidStudentError("Score must be between 0 and 100")
        
except FileNotFoundError:
    print("Student file not found")

except json.JSONDecodeError:
    print("Student file contains invalid JSON")

except InvalidStudentError as e:
    print("Invalid student:", e)

else:
    print("Students loaded successfully")

    for student in loaded_students:
        print(student["name"], student["score"])