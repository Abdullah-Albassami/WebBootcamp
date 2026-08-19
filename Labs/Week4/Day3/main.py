# # Week 4 Day 3 ==> Continuing Day 2 Topic
# CSV Stores rows and columns
# import csv

# with open("students.csv", "w",
#           encoding="utf-8", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["name", "course"])
#     writer.writerow(["Sara", "Python"])
#     writer.writerow(["Ali", "Django"])

# # JSON Preserves list and dictionaries
# import json

# students = [
#     {"name": "Sara", "score": 92},
#     {"name": "Ali", "score": 85}
# ]

# with open("students.json", "w", encoding="utf-8") as file:
#     json.dump(students, file, indent =2)

# with open ("students.json", "r", encoding="utf-8") as file:
#     loaded = json.load(file)

# print(loaded[0]["name"])

# # try and except Define a Failure Path
# try:
#     score = int(input("Score: "))
# except ValueError as e:
#     print("Enter a whole number")
#     print(e)

# print("Program continues")

# # Catch the specific file failure you expect

# from pathlib import Path
# try:
#     text = Path("students.txt").read_text(encoding="utf-8")

# except FileNotFoundError:
#     print("Student file not found")
# except PermissionError:
#     print("Student file can not be read")

# # else and finaly complete the exception flow
# from pathlib import Path

# path = Path("students.txt")

# try:
#     text = path.read_text(encoding="utf-8")
# except OSError as error:
#     print("Load failed: ", error)

# else:
#     print(text)
# finally:
#     print("Load attempt finished")

# Exception Block Have Different jobs

# # raise rejects invalid data immediatlly
# def validate_score(score):
#     if not 0 <= score <= 100:
#         raise ValueError("Score must be 0 to 100")
#     return score

# try:
#     score = validate_score(120)

# except ValueError as error:
#     print(error)

# # Custum Exceptions Express Domain Failures
# class StudentNotFoundError(Exception):
#     pass

# def find_student(name, students):
#     for student in students:
#         if student["name"] == name:
#             return student
#     raise StudentNotFoundError(name)

# students = [{"name": "Sara"}]

# try:
#     print(find_student("Ali", students))
# except StudentNotFoundError as error:
#     print("Missing student:", error)

# File Code Fails when Assumptions stay hidden

# # LAB 1
# class Ticket:
#     def __init__(self, name, status = "Open"):
#         self.name = name
#         self.status = status

#     def newStatus(self, status):
#         self.status = status

# myTicket1 = Ticket("1000", "In-Progress")
# myTicket2 = Ticket("1001", "Pending")

# print(myTicket1.status)
# print(myTicket2.status)

# # LABS Review for classes
# # LAB 2
# class Greeter:
#     def __init__(self, message):
#         self.message = message

#     def greet(self, user):
#         self.user = user

#         return (f"Hello {user}, {self.message}")

# mygreet = Greeter("Welcome to Tuwiqe")

# mygreet.greet("Salem")
# g = mygreet.greet("Salem")
# print(g)

# # LAB 3
# class Welcome:
#     def __init__(self, name):
#         self.name = name

#     def welcome(self):
#         print(f"Welcome {self.name}")

# students = [
#     Welcome("Abdullah"),
#     Welcome("Sara"),
#     Welcome("Omar")
# ]

# for s in students:
#     # s.name = "Old Student"
#     s.welcome()

# # LABS for file handling
# # LAB 1
# from pathlib import Path

# path = Path("home") / "students" / "students.txt" 

# path.parent.mkdir(parents=True, exist_ok=True)

# print(path.is_dir())
# print(path.suffix)
# print(path.name)
# print(path.is_file())

# path.write_text("Welcome to class", encoding="utf-8")
