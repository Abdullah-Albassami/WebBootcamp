# Week 3 Day 2 ==>>


# Names Refer to Objects inside a namesapce

# The same name can exist in different scopes

# LAB 1
course = "Web Development Bootcamp"
duration = 12

def type(course):

    print("Opss!")

    print(course)

    print(duration)

print(type(course)) #it will overwrite the built in function because it is the nearst
print(globals()) # what does it return? check it out

# Each Function call, creates a fresh local Namespace

# LAB 8
def inspect_order(item, qty):

    subtotal = 25 * qty

    print(locals())
    print(locals()["subtotal"])

inspect_order("Pen", 10)

# LEGB is Python's name lookup order (Local, Enclosing, Global, then Built-in), python searches nearby scopes first

# LAB 5 just a sample practicing method
def printer():
    print("Welcome")

def desk():
    printer()

def room():
    desk()

def house():
    room()

def city():
    house()

def country():
    city()


country()
city()
house()

# Local scope belongs to the current function call

# LAB 6
Language = "Python"

def show_lang(language):

    print(language)

show_lang("Dart")

print(Language)

# Enclosing scope appears in nested functions

# LAB 3
def outter():
    location = "Outter"
    print(f"From {location}")

    def inner():
        location = "Inner"
        print(f"From {location}")

    inner()

outter()

# LAB 3.1 # this wold cause an error for some reason find out
def outter():
    location = 1
    print(f"From {location}")

    def inner():
        location += 2
        print(f"From {location}")
    inner()

outter()

# global scope belongs to the current module

# LAB 2
building = "Tuwaiq Academy"
cohort_size = 20

print(f"Welcome to {building}, class limit is {cohort_size}")

print("Tuwaiq" in building)

print("cohort_size" in globals())

print(globals(), ["building"]) # or ["course"] <=learn more

#shift + alt + down

# LAB 7
rate = 0.15

def getTotal(amount):
    total = amount * rate + amount
    return total

print(f"{getTotal(200.3):.2f}")

print(round(getTotal(200.3), 2))

# Built-in scope supplies python's standard names

# shadowing hides a name from an outer scope: a nearer name can hide an outer name

# use shared state deliberately: (Read, change, prefer)

# LAB 4
def outter():
    location = 1
    print(f"From {location}")

    def inner():
        nonlocal location
        location += 2 # try location = 2
        print(f"From {location}")

    inner()

outter()

# Modules keep related code in seprate files
# A module is a reusable Python file.
# Modules reduce duplication and keep programs easier to navigate.
# import import brings selected names into scope, like: from math import sqr,
# aliases make long or conflicting names clearer
# The standerd library provides ready-made modules
# Standard-library modules ship with Python and do not need pip installation.
# Examples: math, random, datetime, statistics, pathlib
# Your own python file can become a module
# The main guard separates running from importing
# When a file runs directly, __name__ is "__main__".
# When a file is imported, __name__ is the module's name.
# The main guard is useful for demos, tests, and program entry code.
# imports connect to package managment
# Module: a .py file that organizes reusable Python names.
# Package: a directory that groups related modules under one import path.
# Dependency: third-party code installed in the active environment
# and recorded so it can be installed again later.
# Import Errors Ususally have a traceable causes
# Read the exception first, then check the module name,
# environment, and project structure.
# Avoid filenames that conflict with standard-library modules:
# random.py
# math.py
# statistics.py
# ImportError:
# Verify that the requested name actually exists in the module.
# ModuleNotFoundError:
# Check the spelling, file/package location, and active environment.
# Circular imports:
# Occur when modules depend on each other while they are loading.