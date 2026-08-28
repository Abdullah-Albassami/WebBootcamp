from pathlib import Path
import json
import csv

# # Task 1
# path = Path("data") / "students" / "scores.txt"
# print(path)
# print(path.name)
# print(path.suffix)

# # Task 2
# path = Path("data") / "students"
# path.mkdir(parents=True, exist_ok=True)
# print(path.exists())
# print(path.is_dir())

# # Task 3
# path = Path("data") / "students" / "names.txt"

# with path.open("x",  encoding="utf-8") as file:
#     file.write("Sara\nOmar")

# # Task 4
# path = Path("data") / "students" / "names.txt"

# with path.open("r", encoding="utf-8") as f:
#     print(f.read())

# # Task 5
# path = Path("data") / "students" / "names.txt"

# text = path.read_text(encoding="utf-8")
# print(text)

# # Task 6
# path = Path("data") / "students" / "names.txt"

# with path.open("r", encoding="utf-8") as f:
#     for line in f:
#         print(f"student: {line.strip()}")

# # Task 7
# path = Path("data") / "students" / "names.txt"
# with path.open("w", encoding="utf-8") as f:
#     f.write("Ali\nNorah\n")
# print(path.read_text(encoding="utf-8"))

# # Task 8
# path = Path("data") / "students" / "names.txt"

# with path.open("a", encoding="utf-8") as f:
#     f.write("Sara")

# print(path.read_text(encoding="utf-8"))

# # Task 9
# path = Path("data") / "students" / "names.txt"
# with path.open("r", encoding="utf-8") as f:
#     print(f.closed)
# print(f.closed)

# # Task 10
# path = Path("data") / "students" / "grades.txt"
# print(path.exists())
# print(path.is_file())
# if path.is_file() and path.exists():
#     print(path.read_text(encoding="utf-8"))
# else:
#     print("File unavailable")

# # Task 11

# p = Path("data") / "students" / "students.csv"
# with p.open("w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["name", "course"])
#     writer.writerow(["Sara", "Python"])
#     writer.writerow(["Omar", "Django"])
# print(p.read_text())
    
# # Task 12
# p = Path("data") / "students" / "students.csv"
# with p.open("r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     # print(list(reader)) # this will consume the csv file
#     for r in reader:
#         print(r)

# # Task 13

# p = Path("data") / "students" / "students.json"
# students = [
#     {"name": "Sara", "score": 92},
#     {"name": "Omar", "score": 85}
# ]
# with p.open("w", encoding="utf-8") as f:
#     d = json.dump(students, f ,indent=2)

# # Task 14
# p = Path("data") / "students" / "students.json"

# with p.open("r", encoding="utf-8") as f:
#     loaded = json.load(f)
#     print(loaded[0]["score"]) # print only Sara's score.

# # Task 15
# try:
#     p = int(input("Enter a number: "))
#     print(p)
# except ValueError as e:
#     print(e, "Enter a whole number")

# # Task 16
# p = Path("data") / "students" / "missing.txt"
# try:
#     p.read_text()
# except FileNotFoundError as fnfe:
#     print(fnfe)

# # Task 17
# p = Path("data") / "students" / "missing.txt"
# try:
#     p.read_text(encoding="utf-8")
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("Permission denied")

# # Tasks 18 & 19
# p = Path("data") / "students" / "names.txt"
# try:
#     re= p.read_text(encoding="utf-8")
# except FileNotFoundError:
#     print("File not found")
# else:
#     print(re)
# finally:
#     print("Read attempt finished") #part of task 19

# # Tasks 20 & 21
# def validate_score(score):
#     if score < 0 or score > 100:
#         raise ValueError("Score must be 0 to 100")
#     return score

# try:    # part of Task 21
#     print(validate_score(190))
# except ValueError as ve:
#     print(ve)

# # Task 22 & 23
# class StudentNotFoundError(Exception):
#     pass

# students = [
#     {"name": "Sara"},
#     {"name": "Omar"}
# ]
# def find_student(name, students):
#     for s in students:
#             if s["name"] == name:
#                 return s
#     raise StudentNotFoundError("no student with this name")

# try:    
#     print(find_student("Ali", students))
# except StudentNotFoundError as e:
#      print(e)

# Task 24 — Comprehensive Practice
# Part 1
p = Path("data") / "students" / "students.json"
p.parent.mkdir(parents=True, exist_ok=True)

students = [
    {"name": "Sara", "score": 92},
    {"name": "Omar", "score": 85},
    {"name": "Ali", "score": 76}
]

# with p.open("w", encoding="utf-8") as f:
#     json.dump(students, f, indent=2)

# print(p.read_text(encoding="utf-8"))
# # Part 2
# def load_students(path):
#     try:
#         with path.open("r", encoding="utf-8") as f:
#             loaded = json.load(f)
#         return loaded
#     except FileNotFoundError as nf:
#         print(nf)
#     except json.JSONDecodeError as invalidJSON:
#         print(invalidJSON)

# readIt = load_students(p)
# print(readIt)
# part 3

def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError("A score must be between 0 and 100")
    return score

vScore1 = validate_score(100)
print(vScore1)
vScore = validate_score(120)
print(vScore)
        


    