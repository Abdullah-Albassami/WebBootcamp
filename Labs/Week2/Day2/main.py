# WEEK 2 DAY 2 ==> VARIABLES, DATA TYPES, INPUT, AND BASICS

# TOPIC 1 — VARIABLES STORE VALUES
# Variables are names that refer to values.
# Variable names are case-sensitive.
# Student_name and student_name are two different variable names.

# Lab 1
Student_name = "Abdullah"
student_name = "Omar"

print("First student:", Student_name)
print("Second student:", student_name)


# TOPIC 2 — CONDITIONAL STATEMENTS CONTROL PROGRAM FLOW
# if checks a condition.
# else runs when the if condition is False.

# Lab 2
score = 95

if score >= 90:
    print("Excellent")
else:
    print("Thank you")


# TOPIC 3 — CONSTANTS USE UPPERCASE BY CONVENTION
# Python does not have true constants.
# UPPERCASE names are used by convention for values that should not change.

MAX_CLASS_SIZE = 25
MIN_CLASS_SIZE = 15


# TOPIC 4 — MULTIPLE ASSIGNMENT ASSIGNS MULTIPLE VALUES AT ONCE
# Python can assign multiple values to multiple variables in one line.

# Lab 3
student_name, student_age, student_is_registered = "Nasser", 24, True


# TOPIC 5 — TYPE() RETURNS THE TYPE OF AN OBJECT
# type() tells us the data type of an object.
# isinstance() checks whether an object belongs to a specific type.

# Lab 4
print(type(student_name))
print(type(student_age))
print(type(student_is_registered))
print("Is age an integer?", isinstance(student_age, int))


# TOPIC 6 — INPUT() ALWAYS RETURNS A STRING
# input() receives user input as a string.
# Type casting converts a value from one type to another.
# int() converts a valid numeric string into an integer.

# Lab 5
age = input("Enter your age: ")

if isinstance(age, int):
    print("You are", age + 5, "AFTER 5 years")
else:
    print("You are", int(age) + 5, "after 5 years")


# TOPIC 7 — STRING INDEXING ACCESSES INDIVIDUAL CHARACTERS
# Each character in a string has an index.
# Python indexing starts at 0.
# len() returns the number of characters in a string.

# Lab 6
teacher_name = "Faisel"
index = int(input("Select index (0 to 5): "))

if index < len(teacher_name):
    print("The character at index", index, "is:", teacher_name[index])
else:
    print("Out of range! The name only has", len(teacher_name), "characters.")

print("Type of length is:", type(len(teacher_name)))


# TOPIC 8 — MULTIPLE ASSIGNMENT CAN SWAP VALUES
# Python can swap the values of two variables without a temporary variable.

# Lab 7
x = 0
y = 1

x, y = y, x

print("After swapping: x =", x, ", y =", y)