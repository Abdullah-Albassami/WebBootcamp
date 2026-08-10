################################################################
# WEEK 3 DAY 1 -- FUNCTIONS
################################################################

# TOPIC 1 — FUNCTIONS TURN REPEATED LOGIC INTO REUSABLE BEHAVIOR

# Repeated logic becomes harder to read, change, and test as a program grows.
# A function gives a useful block of behavior a name.
# Write the logic once, then call it whenever it is needed.
# def creates a function; parentheses call it.

# Lab 1

def greet():
    print("Welcome to Python")

greet()

# TOPIC 2 — A FUNCTION RUNS ONLY WHEN IT IS CALLED

# A function definition and a function call are separate events.
# Python executes def and creates the function object;
# the function body does not run yet.
# A function runs only when it is called.
# A function call transfers control into the function body.
# The function body runs from top to bottom.
# When the function finishes, control returns to the caller.
# Execution continues with the statement after the function call.

# Lab 2
def show_menu():
    print("1- Coffee")
    print("2- Tea")
    print("3- Zatar")

show_menu()

print("Outside the call")

show_menu()

# Lab 3
def unknowScope():
    print("Line One")

    def gotoFunc():
        print("From within the GoTo")

    print("Where is line 2?")
    gotoFunc()
    print("I'm up here")

unknowScope()

# TOPIC 3 — PARAMETERS LET A FUNCTION RECEIVE DATA

# Parameters let functions accept different inputs.
# A parameter is a variable written in the function definition.
# An argument is the actual value passed when calling the function.
# Parameters and arguments are related, but they are not identical.

# Lab 4
def greet_student(name):
    print(f"Welcome {name}")

greet_student("Sara")
greet_student("Taif")

# TOPIC 4 — POSITIONAL ARGUMENTS MATCH BY ORDER

# Positional arguments are assigned to parameters based on their order.
# The order matters when the values have different meanings.
# Keyword arguments match by parameter name.

# TOPIC 5 — DEFAULT PARAMETERS MAKE SOME ARGUMENTS OPTIONAL

# A default parameter provides a value when an argument is not supplied.
# If an argument is supplied, it replaces the default value.

# Lab 5
def show_booking(destination="Riyadh", nights="1"):
    if nights.isdigit():
        nn = int(nights)
        print(f"""You're traveling to {destination},
and will stay for {nn} nights""")

show_booking()
show_booking("Jeddah")
show_booking("Doha", 2)

# TOPIC 6 — RETURN SENDS A RESULT BACK TO THE CALLER

# return ends the current function call and sends a value back to the caller.
# A returned result can be stored in a variable and reused.
# A function without a return statement returns None.

# TOPIC 7 — RETURN AND PRINT SERVE DIFFERENT PURPOSES

# return sends a result back to the caller.
# print displays output to the user.
# print does not return the value that it displays.
# Return program results.
# Print when the goal is visible output.

# TOPIC 8 — FUNCTIONS PACKAGE CALCULATIONS BEHIND CLEAR NAMES

# Functions can package calculations so the same calculation can be reused.

# TOPIC 9 — DOCSTRINGS EXPLAIN WHAT A FUNCTION PROMISES

# A docstring is a string placed first inside a function body.
# A function's docstring can be accessed using function_name.__doc__.
# help(function_name) can also display information about the function.

# Lab 6
def getVAT(total, rate=0.15):
    """This Function will get the total with VAT added
    to it, and return the sum"""
    not_subtotal = total + (total * rate)
    return not_subtotal

print(getVAT(154))
print(getVAT(154, 0.05))
print(getVAT.__doc__)

help(getVAT)

total = getVAT(680)
print(total)

# TOPIC 10 — CLEAR FUNCTIONS ARE EASIER TO READ, REUSE, AND TEST

# Give functions clear names that describe what they do.
# A useful guideline for functions:
# Verb, input, focus.

# TOPIC 11 — FUNCTION ERRORS USUALLY COME FROM MISMATCHED CONTRACTS

# Most beginner function errors come from definitions, calls,
# arguments, and results not matching.
# Provide every required argument.
# Check positional argument order when values have different meanings.
# Do not confuse printed output with a returned result.
# Remember that return ends the current function call immediately.
# Define the function before its call is reached in the execution path.

# TOPIC 12 — FUNCTIONS CAN CONTAIN CONTROL FLOW YOU ALREADY KNOW

# Functions organize logic; they do not replace if statements or loops.
# A function can contain if / elif / else statements.
# A function can also contain loops.
# Parameters provide the input and return exposes the final result.
# Combining earlier concepts creates small, reusable program components.

# Example
def count_even(limit):
    count = 0

    for number in range(1, limit + 1):
        if number % 2 == 0:
            count += 1

    return count

print(count_even(10))

