################################################################
# Exercise — Calculate Grade
################################################################

# Define calculate_grade(score).
# Use score as the function parameter.
# Use if / elif / else to select A, B, C, D, or F.
# Return the grade instead of printing it inside the function.
# Call the function with several scores and print the returned grades.

def calculate_grade(score = ""):
    score = score.strip()
    if not score:
        return "Please Enter a Score! "
    elif not score.isdigit():
        return "Please Enter a number! "
    elif (int(score) >= 90):
        return "A"
    elif (int(score) >= 80):
        return "B"
    elif (int(score) >= 70):
            return "C"
    elif (int(score) >= 60):
            return "D"
    else:
            return "F"

print(calculate_grade(" "))
print(calculate_grade("kk"))
print(calculate_grade("80"))
print(calculate_grade(" 30 "))