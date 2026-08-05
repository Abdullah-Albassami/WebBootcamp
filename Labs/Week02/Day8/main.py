# =========================================================
# DAY 08 — OPERATORS, STRINGS, MUTABILITY, AND IDENTITY
# =========================================================

# TOPIC 1 — ARITHMETIC OPERATORS AND PEMDAS

# (+ Addition) (- Subtraction) (* Multiplication) (/ Division) 
# (// Floor division) (% Remainder) (** Exponent)

# PEMDAS:
# Parentheses
# Exponents
# Multiplication and Division
# Addition and Subtraction

# Lab01 — Operator precedence
result = 10 + 5 * 2 - 4 / 2
print(result)  # 18.0


# Lab02 — Floor division and remainder
total_items = 17
box_capacity = 5

full_boxes = total_items // box_capacity
remaining_items = total_items % box_capacity

print(f"You can fill {full_boxes} full boxes")
print(f"You will have {remaining_items} items remaining")


# Lab03 — Effect of parentheses
base_calc = 2 + 3 * 2 ** 2
grouped_calc = (2 + 3) * 2 ** 2

print(base_calc)     # 14
print(grouped_calc)  # 20


# Arithmetic exercise
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)


# TOPIC 2 — COMPARISON OPERATORS

# Comparison operators produce Boolean values: True or False

print(5 == 5)  # True
print(5 != 3)  # True
print(10 > 4)  # True

# TOPIC 3 — LOGICAL OPERATORS

# and — both conditions must be True
# or  — at least one condition must be True
# not — reverses a Boolean value


# Lab04 — Combining conditions
user_age = 25
has_permission = True

is_eligible = user_age >= 18 and has_permission
print(f"Eligibility status: {is_eligible}")


# The same condition using a conditional expression
is_eligible = True if user_age >= 18 and has_permission else False
print(is_eligible)


# The same logic using nested if statements
if user_age >= 18:
    if has_permission:
        is_eligible = True


# TOPIC 4 — ASSIGNMENT OPERATORS

# +=  Add and assign
# -=  Subtract and assign
# *=  Multiply and assign
# /=  Divide and assign

# Lab05
score = 10

score += 5       # Same as: score = score + 5
score *= 5       # Same as: score = score * 5

print(f"Your score is {score}")


# TOPIC 5 — MEMBERSHIP OPERATORS

# in     Checks whether a value exists
# not in Checks whether a value does not exist
# Membership checks are case-sensitive


# Lab06
memberships = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"

if current_membership in memberships:
    print("Welcome")
else:
    print("Go Home")


print("Admin" in memberships)       # True
print("admin" in memberships)       # False
print("Guest" not in memberships)   # True


# TOPIC 6 — STRING METHODS

# String methods transform or inspect text.
# Strings do not change unless the returned value is stored.

raw = "   Python Bootcamp   "

print(raw.strip())                       # Removes surrounding spaces
print(raw.lower())                       # Converts to lowercase
print(raw.upper())                       # Converts to uppercase
print(raw.replace("Bootcamp", "Course"))
print(raw.find("Python"))
print(raw.startswith("Python"))
print(raw.endswith("Bootcamp"))


# Lab07 — find()
sentence = "Python Web Development"
position = sentence.find("t")

print(position)

# TOPIC 7 — INDEXING AND SLICING


# Indexing retrieves one character.
# Slicing retrieves a range of characters.

# General syntax: text[start:stop:step]

# Lab08
message = "Python Programming"

first_char = message[0]
last_char = message[-1]

print(
    f"First character is {first_char} "
    f"and last character is {last_char}"
)

sliced_message = message[:6]
reversed_message = message[::-1]

print(sliced_message)

print(f"""
Your message was {message}.
The first 6 characters are {sliced_message}.
The reversed message is {reversed_message}.
""")


# Slicing exercise
sentence = input("Enter a sentence: ")

print(sentence[:5])      # First 5 characters
print(sentence[5:])      # Everything after the first 5
print(sentence[-5:])     # Last 5 characters
print(sentence[::-1])    # Reversed sentence


# TOPIC 8 — COMMON STRING METHODS

sentence = input("Enter another sentence: ")

print(sentence.upper())
print(sentence.lower())
print(sentence.replace("Python", "Java"))
print(sentence.find("Python"))
print(sentence.count("a"))
print(sentence.strip())


# Lab09 — Cleaning and formatting strings
my_email = "   faisal@eXample.com   "

cleaned_email = my_email.strip().lower()

message = "python web development"
titled_message = message.title()

print(
    f"Your email is {cleaned_email}, "
    f"and your course is {titled_message}"
)

# TOPIC 9 — split() AND join()

# split() converts a string into a list.
# join() combines a list of strings into one string.

csv_line = "Ali,Sara,Omar"

names = csv_line.split(",")
print(names)

joined_names = " | ".join(names)
print(joined_names)


# Lab10
csv_text = "apple,orange,banana,cherry,dates"

split_text = csv_text.split(",")
print(split_text)

joined_text = " | ".join(split_text)

print(f"""Your text is:
{csv_text}

Split like this:
{split_text}

Rejoined like this:
{joined_text}
""")

# TOPIC 10 — MUTABLE AND IMMUTABLE OBJECTS

# Mutable objects can be changed after creation.
# Examples: (list, dict, set)

numbers = [1, 2, 3]
numbers[0] = 10

print(numbers)


# Immutable objects cannot be changed after creation.
# Examples: (str, int, float, tuple, bool)

# Lab11 — Strings are immutable
name = "Khalid"

try:
    name[0] = "A"
except TypeError as error:
    print(error)


# To create "Ahalid", make a new string instead:
new_name = "A" + name[1:]
print(new_name)


# TOPIC 11 — VALUE EQUALITY AND OBJECT IDENTITY

# == compares values.
# is compares whether two names reference the same object.

first = [1, 2]
second = [1, 2]
alias = first

print(first == second)  # True: same values
print(first is second)  # False: different objects
print(first is alias)   # True: same object


# Object identity tracks the object, not the variable name.

x = [5]
y = [5]

if x == y:
    print("x and y contain the same value")

if x is not y:
    print("x and y are different objects")

print(id(x))
print(id(y))


# TOPIC 12 — replace(), SWAPPING, AND None

# Lab12 — replace()
message = "Python Web Development"

new_message = message.replace(
    "Development",
    "Programming"
)

print(new_message)


# Swapping variable values
x = 5
y = 6

x, y = y, x

print(x)  # 6
print(y)  # 5


# None represents the absence of a value.
is_online = None

if is_online is True:
    print("True")
elif is_online is False:
    print("False")
else:
    print("None")


# Use "is None" instead of "== None"
if is_online is None:
    print("No online status has been assigned")