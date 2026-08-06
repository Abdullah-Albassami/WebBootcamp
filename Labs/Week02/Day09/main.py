# =========================================================
# DAY 09 — CONDITIONAL STATEMENTS
# =========================================================

# TOPIC 1 — IF STATEMENTS

# Conditions control the program's path.
# if runs code only when its condition is True.

# Lab01 — Simple if

age = 20

if age >= 18:
    print("Welcome")

print("Code completed")


# TOPIC 2 — IF / ELSE

# else creates the alternative path when the condition is False.

# Lab02 — if / else

temperature = 31

if temperature >= 35:
    print("It's hot outside")
else:
    print("Cool")

# TOPIC 3 — ELIF

# elif allows several possible outcomes.
# The first True branch wins.

# Lab03 — if / elif / else

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("You need to improve")

# TOPIC 4 — LOGICAL OPERATORS

# Build more complete conditions.
# and → both conditions must be True.
# or  → at least one condition must be True.
# not → reverses a Boolean value.

# Lab04 — Logical operators

is_active = True
is_verified = True
role = "Editor"
is_blocked = False

if is_active and is_verified:
    print("Account is ready")

if role == "Admin" or role == "Editor":
    print("User can edit")

if not is_blocked:
    print("User is not blocked")
else:
    print("User is blocked")


# TOPIC 5 — NESTED CONDITIONS

# Nested conditions represent dependent decisions.

# Lab05 — Nested if

account_active = True
has_permission = True

if account_active:
    if has_permission:
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Account is not active")


# TOPIC 6 — TRUTHY AND FALSY VALUES

# Objects can evaluate to True or False.
# Empty values are usually False.
# Non-empty values are usually True.

# Lab06 — Truthy / Falsy

name = "Faisal"
cart = []
balance = 990

if name:
    print("Name has a value")

if not cart:
    print("Your cart is empty")

print(bool(balance))

# TOPIC 7 — INPUT VALIDATION

# Validation protects the program's assumptions.
# Common text validation methods:
# strip()
# isdigit()
# isalpha()

# Lab07 — Name validation

name = input("Enter your first name: ").strip()

if not name:
    print("Please enter a name")
elif not name.replace(" ", "").isalpha():
    print("Name must contain letters")
else:
    print(f"Valid name: {name}")

# Lab08 — Numeric validation

age_text = input("Enter your age: ").strip()

if age_text.isdigit():
    age = int(age_text)
    print(f"You will be {age + 5} in 5 years")
else:
    print("Please enter a valid number")

# Lab09 — Range validation

score_text = input("Enter a score between 0 and 100: ").strip()

if score_text.isdigit():
    score = int(score_text)

    if 0 <= score <= 100:
        print("Valid score")
    else:
        print("Invalid score")
else:
    print("Please enter a valid number")

# TOPIC 8 — MEMBERSHIP VALIDATION
# Use membership operators to validate choices.
# in
# not in

# Lab10 — Membership operator

memberships = ["Admin", "Editor", "Viewer"]

current_membership = input("Enter your membership: ").strip().title()

if current_membership in memberships:
    print("You are allowed to view the content")
else:
    print("Please contact the admin team")

# TOPIC 9 — CONDITIONAL EXPRESSIONS

# Conditional expressions keep simple choices compact.
#
# Syntax:
# value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"

print(status)

# TOPIC 10 — MATCH STATEMENT

# match simplifies fixed-choice branching.
# case _ acts as the default branch.


# Lab11 — Match statement

command = input(
    "Enter a command (start, stop, status): "
).strip().lower()

match command:
    case "start":
        print("Starting system...")
    case "stop":
        print("Stopping system...")
    case "status":
        print("System is running")
    case _:
        print("Unknown command")

