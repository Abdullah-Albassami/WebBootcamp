# WEEK4 - DAY1 ==> OOP Foundations Classes & Objects

# Objects keep related data and behavior together
# A class defines a reusable object type
# class Student:
#     pass
# print(Student)
# print(type(Student))
# # calling a class creates an object

# class Student:
#     pass

# student_one = Student()
# student_two = Student()

# print(student_one)
# print(student_one is student_two)
# # __init__Establishes the Starting State
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# student = Student("Sara", 92)

# print(student.name)
# print(student.score)

# # self Refers to the current object
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def interduce(self):
#         print(f"I am {self.name}") # it is a bad practice to use print insde of a class

# student = Student("Omar")
# student.interduce()
        
# # Instance attributes belong to one object
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# sara = Student("Sara", 92)
# omar = Student("Omar", 81)

# sara.score = 95
# print(sara.score)
# print(omar.score)
# print(omar is sara)
# print(isinstance(omar, Student))

# # Class attributes are shared defaults
# class Student:
#     academy = "Tuwaiq Academy"

#     def __init__(self, name):
#         self.name = name

# sara = Student("Sara")
# print(Student.academy)
# print(sara.academy)

# # Instance methods define object behavior
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def display_result(self):
#         print(self.name, self.score)

# student = Student("Lina", 88)
# student.display_result()

# # Methods can change object state
# class Counter:
#     def __init__(self):
#         self.value = 0
#     def increment(self):
#         self.value += 1

# counter = Counter()
# counter.increment()
# counter.increment()
# print(counter.value) # 2

# # Methods can Return calculated values
# class Rectangular:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height

# rectangular = Rectangular(5, 3)

# print(rectangular.area())

# # Methods can protect valid state
# class BankAccount:
#     def __init__(self, balance = 0):
#         self.balance = balance
#     def withdraw(self, amount):
#         if amount <= 0 or amount > self.balance:
#             return False

#         self.balance -= amount
#         return True

# account = BankAccount(500)
# print(account.withdraw(200))
# print(account.balance)

# # __str__Gives an object a readable description

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def __str__(self):
#         return f"{self.name}: {self.score}"

# student = Student("Sara", 95)
# print(student)

# # Each instance keeps independent state
# class Counter:
#     def __init__(self):
#         self.value = 0
#     def increment(self):
#         self.value += 1

# first = Counter()
# second = Counter()

# first.increment()

# print(first.value) # 1
# print(second.value) # 0

# # Collections Can Store Objects 
# class Student:
#     def __init__(self, name):
#         self.name = name
#     def greet(self):
#         return f"Hello, {self.name}"

# students = [
#     Student("Sara"),
#     Student("Omar"),
#     Student("Lina")
# ]
# # print(students[0].greet())
# for student in students:
#     print(student.greet())

# # type() and isinstance() Identify Object Types

# class Student:
#     pass

# student = Student()
# print(type(student))
# print(type(student) is Student)
# print(isinstance(student, Student)) # The syntax is: isinstance(object, Class)

# Class, Object, and Method Play Different Roles
#  * Class: blueprint that defines shared structure and behavior.
#  * Object: instance that stores its own independent state.
#  * Method: behavior that reads or changes an object's state.

# # Attribute Access Is Public by Default
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self._score = score
#     # def updateScore(self, newScore):
#     #     self._score= newScore

# student = Student("Sara", 95)

# print(student.name)
# print(student._score) # Accessable, but treated as internal
# # student.updateScore = 100
# # print(student.updateScore)

# # A Small Class Keeps Data and Behavior Together
# class Student:
#     def __init__(self, name, scores):
#         self.name = name
#         self.scores = scores

#     def average(self):
#         return sum(self.scores) / len(self.scores)
#     def add_score(self, score):
#         if 0 <= score <= 100:
#             self.scores.append(score)

# student = Student("Sara", [80, 90])
# student.add_score(100)
# print(student.name, student.average())

# OOP Errors Usually Reveal a Broken Object Boundary
#  * Check which object owns the state, which method is being called,and whether initialization completed.
#  * Forgetting self in an instance method causes argument errors.
#  * Using a class attribute for changing instance data can accidentally share state between objects.
#  * Misspelled attributes can create errors or unintended new attributes.
#  * Keep each class focused; do not turn one class into the entire application.
