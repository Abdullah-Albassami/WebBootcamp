# Loops Replace Repetion with a rule
# for repeates code for each item
# range() controls numeric repetition
# range() can count forward or backward
# a for loop can walk through a string 
# a for loop can process a collection 
# conditions decide what happens inside a loop 
# counters record how often something happens
# Accumlators build a result over time 
# while repeates while a conditions is true 
# for and while solve different repetiton problems 
# while can keep asking until input is valid 
# every while loop needs an exit startegy 
# break exits a loop immediately: 
# continue skips only the current iteration 
# pass keeps an empty block syntactically valid 
# nested loops repeat work at more than one level (outer loop, inner loop, work grows)
# a menue shows how the pecies work together 
# loop mistakes have recognizable causes, most loop bugs like (Range, while, indent)
# read the loop before running it (tracing by hand)
# Practice exersies: 
""" count = 0
total = 0
max = int(input(" Enter a max: "))

for i in range(1, max):
    count += 1
    print(f"count is {count}")
    if i % 2 == 0:
        print(i ,"is even")
    else:
        print(i,"is Odd")

print(f"total number of iter is {count}") """


# # LAB 1 
# for attempts in range(3):
#     print(f"Attempts: {attempts + 1}")
# print("Program Completed!")

# # LAB 2
# for num in range(2, 11, 2):
#     print(num)

# # LAB 3 
# for secondsToLaunch in range(10, 0, -1):
#     print(f"T-: {secondsToLaunch}")

# # LAB 4 
# course = "Python"
# for letter in course:
#     print(letter)

# # LAB 5 
# students = ["shahad", "a", "b", "c", "d"]
# for student in students:
#     print(f"Progressing student is: {student}")

# # LAB 6 
# for number in range(1, 11):
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
#     print("------------")
# # LAB 7
# numbers = [4, 7, 10, 13, 16, 21]
# even_counter = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_counter += 1 

# print(f"Total even numbers is: {even_counter}")

# # LAB 8
# prices = [25, 30, 55, 115]
# total = 0

# for price in prices:
#     total += price

# print(f"your total is {total} VAT: {total * (15/100)}") # (1.15:.2f) to show only two decimals

# # LAB 9
# count = 0
# while count <= 5:
#     count += 1
#     print(f"Count...{count}")
# print("Loop Completed!")

# # LAB 10
# message = "Please enter a number: "
# age_text = input("Please enetr your age: ").strip()
# while not age_text.isdigit():
#     age_text = input(message).strip()

# age = int(age_text)

# print(f"you are {age} yours old")

# # LAB 11
# password = "python123"
# print("Please Enter your password")

# while password != "":
#     password = input("Enter your password: ")
    



