import math
# # Week 3 Day 3
# # Collections keep related values together
# # Lists store orered, changeable values
# students = ["Sara", "Omar", "Lina"]

# print(students)
# print(students[0])
# print(type(students))
# # Indexes Select One Item by Position
# colors = ["red", "green", "blue"]

# # Slicing selects a range of items
# numbers = [10, 20, 30, 40 ,50]
# # try [1:4], [:3], [::2], [::-1]

# # Lists can change after creation
# tasks = ["plan", "code"]
# tasks[0] = "design"
# tasks.append("test")
# tasks.insert(1, "Review")

# print(tasks)

# scores = [88, 72, 95, 81]

# scores.remove(72)
# last = scores.pop()
# scores.sort()

# print(scores)
# print(last)

# # Loops process every item in a collection

# students = [ "sara", "omar", "Line"]

# for student in enumerate(students):
#     print(student)

# for index, student in enumerate(students):
#     print(index, student)

# # a collection can contain
# matrix = [
# [1,2,3],
# [4,5,6] 
# ]
# print(matrix[0])
# print(matrix[1][2])

# # tuples store ordered values that should not change

# location = (24.7136, 46.6753)
# print(location[0])
# print(location[-1])
# # location[0] = 25 # TypeError

# # unpacking assigns collection items to names
# student = ("sara", 22, "python", "PC", "Person")
# name, age, course, *other = student # * ==> catch all

# print(name)
# print(age)
# print(course)

# # Sets keep only Unique Values
# skills = {"Python", "Git", "Python"}
# skills.add("Django")
# print(skills)
# print("Git" in skills)
# print(len(skills))

# # Set Operations Compare Groups

# backend = {"Python", "Django", "SQL"}
# frontend = {"HTML", "CSS", "JavaScript", "SQL"}

# print(backend | frontend) # union
# print(backend & frontend) # intersection
# print(backend - frontend) # difference
# print(frontend - backend) # difference

# # Dictionaries Connect Unique Keys to Values
# student = {
#     "name": "Sara",
#     "age": 22,
#     "course": "Pyhton"
# }
# print(student["name"])

# Add, Update, and Remove Dictionary Values

# student = {"name": "Sara", "score": 90}

# student["score"] = 95
# student["grade"] = "A"

# email = student.get("email", "Not set")
# grade = student.pop("grade")
# print(email)
# print(grade)
# print(student)

# # Dictionary Loops Can Read Keys and Values
# student = {"name": "Sara", "score": 95}

# for key in student:
#     print(key)

# for key, value in student.items():
#     print(key, value)

# for value in student.values():
#     print(value)

# # Choose a Collection by Its behavior (Ordered, Unique, )
# # Common Operations Work across Collections
# names = ["Sara", "Omar"]
# skills = {"Python", "Git"}
# student = {"name": "Sara", "score": 95}

# print(len(names))
# print("Python" in skills)
# print("name" in student) # checks keys

# # Nested Collections Model Structured Record
# students = [ 
#     {"name": "Sara", "score": 95},
#     {"name": "Omar", "score": 88}
# ]
# for student in students:
#     print(student["name"], student["score"])

# # collection Errors Usually Reveal the wrong Assumption

# # Exersies

# students = [ 
#     {"name": "Sara", "score": (95, 80, 70), "skills": {"Progarmming", "Hacking", "troubleshooting"}},
#     {"name": "Omar", "score": (99, 83, 75), "skills": {"coding", "english", "designing"}}
# ]

# averge =0.0
# for s in students:
#     x = (sum(s["score"]))
#     y = (len(s["score"]))
#     averge = x / y

# print(averge)


# students[0]["skills"].add("typing")

# # print(f"name: {students[0]["name"]}")
# print(f"{students[0]["skills"]}")

# # Lab1
# students = ["sara", "mash", "Dal", "Taif"]

# for student in students:
#     print(student)

# iterable = enumerate(students)
# print(iterable)

# for iterable in enumerate(students):
#     # print(next(iterable))
#     print(iterable)

# # LAB 2
# set_col = {"Abdullah", "Nasser", "Dala", "Sara"}
# tuple_col = (11,22,33,44,55,66)
# dict_col = {"name": "Abdullah", "age": 22, "has_car": True}
# list_col = ["ABC", 333, (33,33)]
# for c in dict_col.values():
#     print(type(c))
# # print(set_col)
# # print(tuple_col)
# # print(dict_col)
# # print(list_col)
# # print(type(set_col))
# # print(type(tuple_col))
# # print(type(dict_col))
# # print(type(list_col))

# # LAB 3
# cars = ["GMC","BMW","Geely","Porche","Merc","Chevy"]

# print(cars[3])
# print(cars[-1])
# print(cars[-1::-1])

# # LAB 4
# tasks = ["Read email", "Open ticket"]

# tasks[0] = "Login"
# tasks.append("Get Coffee")
# tasks.insert(0, "Get breakfast")
# tasks.pop(3)

# print(tasks)

# LAB 5
nums = [11,22,33,44,55,66]
print(sum(nums))
print(len(nums))
print(max(nums))
print(min(nums))
print(math.sqrt(max(nums)))
print(math.__doc__)
print(nums)
print(nums.pop(2))
print(sorted(nums, reverse=True))

# LAB 6
skills = {"Python", "Django", "Flask", "FastAPI", "Java"}
skills.add("css")
skills.add("HTML")
skills.discard("Java")

print(skills)



