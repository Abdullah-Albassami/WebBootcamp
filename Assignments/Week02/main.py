# First part
student_name = "Abdullah"
student_age = 26
course = "Python"
isRegistered = True

status = "Registered" if isRegistered else "Not Registered"

print(f"""
Name: {student_name}
Program: {course}
Age: {student_age}
Registration: {status}
""")

print(f"""
Welcome {student_name} to the {course} course!
You are {student_age} years old
Your current registration status is: {status}
Thank you {student_name} and best of luck!
""")

# Second part
x, y = 0, 1
x, y = y, x
print(f"""
x = {x} 
y = {y}""")


