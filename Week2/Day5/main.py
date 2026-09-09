# # =========================================================
# # WEEK 2 DAY 5 — LOOPS
# # =========================================================

# # TOPIC 1 — FOR LOOPS

# # Loops replace repeated code with a rule.
# # A for loop repeats code once for each item in a sequence.
# # Syntax:
# # for item in sequence:
# #     code

# # Lab01 — Repeat a fixed number of times
# for attempt in range(3):
#     print(f"Attempt: {attempt + 1}")
# print("Program Completed!")

# # TOPIC 2 — RANGE()

# # range() generates a sequence of numbers for a loop.
# # range(stop)
# # range(start, stop)
# # range(start, stop, step)
# # The stop value is NOT included.

# # Lab02 — Count using a step
# for num in range(2, 11, 2):
#     print(num)

# # Lab03 — Count backward
# # A negative step makes range() count backward.
# for seconds_to_launch in range(10, 0, -1):
#     print(f"T-{seconds_to_launch}")

# # TOPIC 3 — LOOPING THROUGH STRINGS

# # A for loop can walk through a string one character at a time.

# # Lab04 — Loop through characters
# course = "Python"
# for letter in course:
#     print(letter)

# # TOPIC 4 — LOOPING THROUGH COLLECTIONS

# # A for loop can process each item in a collection such as a list.

# # Lab05 — Loop through a list
# students = ["Shahad", "A", "B", "C", "D"]
# for student in students:
#     print(f"Processing student: {student}")

# # TOPIC 5 — CONDITIONS INSIDE LOOPS

# # Conditions decide what happens during each iteration.
# # This allows different items to be handled differently.

# # Lab06 — Identify even and odd numbers
# for number in range(1, 11):
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")
#     print("------------") 

# # TOPIC 6 — COUNTERS

# # A counter records how many times something happens.
# # Start the counter before the loop and update it when needed.

# # Lab07 — Count even numbers
# numbers = [4, 7, 10, 13, 16, 21]
# even_counter = 0
# odd_counter = 0

# for num in numbers:
#     if num % 2 == 0:
#         print(f"even: {num}")
#         even_counter += 1
#     else:
#         print(f"odd: {num}")
#         odd_counter += 1

# print(f"Total even numbers: {even_counter}")
# print(f"Total odd numbers: {odd_counter}")

# # TOPIC 7 — ACCUMULATORS

# # An accumulator builds a result over time.
# # A common example is adding values to a running total.

# # Lab08 — Calculate a running total
# prices = [25, 30, 55, 115, 3]
# total = 0

# for price in prices:
#     total += price

# print(f"your total is {total} VAT: {total * (15/100):.2f}") # ((15/100):.2f) to show only two decimals

# # TOPIC 8 — WHILE LOOPS

# # A while loop repeats as long as its condition remains True.
# # for loops are useful when the number of repetitions is known.
# # while loops are useful when repetition depends on a condition.
# # Syntax:
# # while condition:
# #     code

# # Lab09 — Repeat while a condition is True
# count = 0

# while count <= 5:
#     count += 1
#     print(f"Count...{count}")

# print("Loop Completed!")

# # TOPIC 9 — INPUT VALIDATION WITH WHILE

# # A while loop can keep asking for input until it becomes valid.
# # The input must be collected again so the condition can change.

# # Lab10 — Keep asking until a number is entered
# message = "Please enter a number: "
# age_text = input("Please enter your age: ").strip()

# while not age_text.isdigit():
#     age_text = input(message).strip()

# age = int(age_text)
# print(f"You are {age} years old")

# # TOPIC 10 — WHILE LOOP EXIT STRATEGIES

# # Every while loop needs an exit strategy.
# # A loop becomes infinite if its condition never becomes False.
# # Common causes:
# # - A counter is never updated.
# # - Input is never collected again.
# # - The wrong variable is checked.
# # Ask: "What must change for this condition to become False?"

# # Lab11 — Stop when the condition becomes False
# password = input("Please enter your password: ")

# while password != "python123":
#     password = input("Enter your password: ")

# print("Access Granted!")

# # TOPIC 11 — BREAK

# # break exits the nearest loop immediately.
# # while True creates a loop that continues until deliberately stopped.

# Lab 12
for badscore in [80, 45, 55, 90]:
    if badscore < 50:
        break
    print(f"We saw: {badscore}")

# # TOPIC 12 — PASS

# # pass does nothing.
# # It keeps an empty block syntactically valid.

# # Lab 12
# for score in [80, 55, 45, 90]:
#     if score < 50:
#         pass
#     print(f"If passes the {score}")

# # TOPIC 13 — CONTINUE

# # continue skips the rest of the current iteration and moves
# # to the next iteration.

# # Lab 12
# for record in [80, 55, 45, 90]:
#     if record < 50:
#         continue
#     print(f"If passes the {record}")

# # TOPIC 14 — NESTED LOOPS

# # A nested loop is a loop inside another loop.
# # For each outer-loop iteration, the inner loop runs completely.
# # More nesting means more total work.

# # Example
# for row in range(1, 4):
#     for column in range(1, 4):
#         print(f"Row: {row}, Column: {column}")
# # Lab 13
# for row in range(1, 4):
#     for column in range(1,4):
#         print(f"{row} X {column} = {row * column}")

# # TOPIC 15 — LOOP DEBUGGING AND TRACING

# # Common loop problems:
# # - Incorrect range() start, stop, or step.
# # - A while condition that never becomes False.
# # - Forgetting to update a counter or variable.
# # - Incorrect indentation.
# # Trace loops by checking the starting value, condition,
# # what changes each iteration, and when the loop stops.


