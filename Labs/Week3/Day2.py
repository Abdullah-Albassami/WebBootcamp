# Week 3 Day 2 ==>> 
# Names Refer to Objects inside a namesapce
# The same name name can exist in different scopes
# Each Function call, creates a fresh local Namespace
# LEGB is Python's name lookup order (Local, Enclosing, Global, then Built-in), python searches nearby scopes first
# Local scope belongs to the current function call
# Enclosing scope appears in nested functions
# global scope belongs to the current module
# Built-in scope supplies python's standard names
# shadowing hides a name from an outer scope: a nearer name can hide an outer name
# use shared state deliberately: (Read, change, prefer)
# Modules keep related code in seprate files
# import import brings selected names into scope, like: from math import sqr, 
# aliases make long or conflicting names clearer
# The standerd library provides ready-made modules
# Your own python file can become a module
# The main guard separates running from importing
# imports connect to package managment
# Import Errors Ususally have a traceable causes

# # LAB 1
# course = "Web Development Bootcamp"
# duration = 12

# def type(course):
#     print("Opss!")

# print(course)
# print(duration)
# print(type(course)) #it will overwrite the built in function because it is the nearst
# print(globals()) # what does it return? check it out

# # LAB 2
# building = "Tuwaiq Academy"
# cohort_size = 20

# print(f"Welcome to {building}, class limit is {cohort_size}")
# print("Tuwaiq" in building)
# print("cohort_size" in globals())

# print(globals(), ["building"]) # or ["course"] <=learn more
# #shift + alt + down

# # LAB 3
# def outter():
#     location = "Outter"
#     print(f"From {location}")
#     def inner():
#         location = "Inner"
#         print(f"From {location}")
#     inner()
# outter()

# # LAB 3.1 # this wold cause an error for some reason find out
# def outter():
#     location = 1
#     print(f"From {location}")
#     def inner():
#         location += 2
#         print(f"From {location}")
#     inner()
# outter()

# # LAB 4
# def outter():
#     location = 1
#     print(f"From {location}")
#     def inner():
#         nonlocal location
#         location += 2 # try location = 2
#         print(f"From {location}")
#     inner()
# outter()

# # LAB 5 just a sample practicing method
# def printer():
#     print("Welcome")

# def desk():
#     printer()

# def room():
#     desk()

# def house():
#     room()

# def city():
#     house()

# def country():
#     city()

# country()
# city()
# house()

# # LAB 6
# Language = "Python"

# def show_lang(language):
#     print(language)

# show_lang("Dart")
# print(Language)

# # LAB 7 
# rate = 0.15
# def getTotal(amount):
#     total = amount * rate + amount
#     return total

# print(f"{getTotal(200.3):.2f}")
# print(round(getTotal(200.3), 2))

# # LAB 8
# def inspect_order(item, qty):
#     subtotal = 25 * qty 
#     print(locals())
#     print(locals()["subtotal"])

# inspect_order("Pen", 10)