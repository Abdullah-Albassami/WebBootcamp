# =========================================================
# EXERCISE week 2 day 4 — STUDENT REGISTRATION VALIDATOR
# =========================================================

# Requirements:
# 1. Ask for a student's:
#    - Name
#    - Score
#    - Selected course
#
# 2. Validate the name is not empty.
#
# 3. Validate the score is numeric
#    and between 0 and 100.
#
# 4. Assign a grade using if / elif / else.
#
# 5. Confirm the course using
#    either the membership operator (in)
#    or a match statement.

name = input("Enter your name: ")
score = input("Enter your score: ")
selectedCourse = input("Enter the Course: ")

courses = ["Python", "Math", "History"]

if selectedCourse not in courses:
    print("Courses doesnt exist!")

if not name:
    print("Please Enter your name")
else:
    name = name.strip()

if score.isalpha():
    print("Please enter a number")
else: 
    score = int(score)
    if score < 0 or score > 100:
        print("The Score must be between 0 and 100")
    elif score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("Failed")








