# Lab01
# pem des
# mutable and immutable
# Comparisions Produce Boolean
# and, or, not, Combine Conditions
# Membership Checks Whether a Value Appears (in, not in, case matters)
# Identity operators Compare object Refernces
'''
first = [1, 2]
second = [1, 2]
alias = first

first == second # True: same value
first is second # False: different objects
first is alias # True: same object

# == and is Ask different questions
# indexing retrives one character
# slicing retrives a range of characters
# String methods transform and ispect text  
# split() and join() reshape text ex csv_line....
csv_line = "Ali,Sara,Omar"
names = csv_line.split(",") # ['Ali', 'Sara', 'Omar']
print(csv_line)

message = " | ".join(names) # 'Ali | Sara | Omar'
print(message)
# object identity tracks the object, not the name (mutable and immutable objects)

# exersise
sentence = input("Enter a sentace: ")
# Slicing
print(sentence[:5])      # First 5 characters
print(sentence[5:])      # Everything after the first 5
print(sentence[-5:])     # Last 5 characters
print(sentence[::-1])    # Reverse the sentence
# split()
words = sentence.split()
print(words)
# join()
words = sentence.split()
new_sentence = "-".join(words)
print(new_sentence)
# upper() / lower()
print(sentence.upper())
print(sentence.lower())
# replace()
print(sentence.replace("Python", "Java"))
# find()
print(sentence.find("Python"))
# count()
print(sentence.count("a"))
# strip()
print(sentence.strip())

# Arthimatic opertors
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Lab0
print(num1 + num2)

total_items = 17
box_capacity = 5

full_box = total_items // box_capacity

# Lab04
user_age = 25
has_permission = True

is_eligiable = (user_age >= 18 and has_permission)
# or is_eligiable = (True if (user_age >= 18 or has_permission) else False)
print(f"Eligiablity status: {is_eligiable}")

# Lab05
score = 10
score += 5
# score = score + 5
score *=5
print(f"Your score is {score}")

# Lab06
# check if the user is one of the values on the list if not go home
memberships = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"
# not current_membership = ["Editor"] check what could happen!
# and try if current_membership[1] in memberships:
if current_membership in memberships:
    print("Welcome")
else: 
    print("Go Home")

# Lab07
sentance = "Python Web Development"
new_sentance = sentance.find("t")

print(new_sentance)

# Lab08
message = "Python Programming"

first_char = message[0]
last_char = message[-1]
print(f"First character is {first_char} and last character is {last_char}")
# Slicing
sliced_message = message[:6]
print(sliced_message)
reversed_message = message[::-1] # message[Start from:end on:number of steps]

print(f"""
Your message was {message},
if we take the first 6 characters it will be {sliced_message},
if we reverse it, it will be {reversed_message}
""")


# Lab09 
my_email = "   faisal@eXample.com.  "
cleaned_email = my_email.strip().lower()
message = "python web development"
titled_message = message.title()
print(f"your emails is {cleaned_email}, and your course is {titled_message}")

# Lab10

csv_text = "apple,orange,bannana,cherry,dates"

splitted

# Lab11
name = "Khalid"
name[0] = "A" # invalid (check it out)

# next topic try except
try:
    name = "Khalid"
except TypeError as e:
    print(e)

x = 5 # x = [5]
y = 5 # y = [5]
if(x == y): # or try if(x is y):
    print("they are the same (if '==' was used) value or (if 'is' was used)object")
else:
    print("they are not the same value or object") 

# x =+ 5
print(y)
print(id(x))
print(id(y))

# Lab12

message = "python web development"
new_message = message.replace("Development", "Programming")

print(new_message)

x = 5
y = 6
x,y = y,x
print(y)
print(x)

is_online = None

if(is_online == None):
    print("True")
elif(is_online != True and is_online != False):
    print("False")
else:
    print("None")
#print(is_online)
    
'''