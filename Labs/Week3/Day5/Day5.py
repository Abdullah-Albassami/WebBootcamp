## WEEK 3 DAY 5 Continus to Day 4

# # A generator expression produces values on demand
# # Parentheses () create the lazy expression.
# # Check next() too.
# # Check the Big O notation for this concept.

# numbers = range(1_000_000)
# total = sum([
#     number ** 2
#     for number in numbers
# ])
# print(total)

# # Mutable Objects Change; Immutable Objects Are Replaced
# items = ["Python", "Git"]
# print(id(items))
# items.append("Django")
# print(id(items))
# name = "sara"
# print(id(name))
# name = name.title()
# print(id(name))

# # Assignment Can Make Two Names Share One Object
# original = ["Python", "Git"]
# alias = original

# alias.append("Django")
# print(original)
# print(alias)
# print(original is alias)

# # Shallow Copy Creates a New Outer Container
# # The purpose is to create a separate outer container so you can modify it without modifying the original.
# original = ["Python", "Git"]
# clone = original.copy()

# clone.append("Django")

# print(original)
# print(clone)
# print(original is clone) # False

# # A Shallow Copy Still Shares Nested Mutable Objects
# original = [["Sara", 90], ["Omar", 85]]
# clone = original.copy()
# clone[0][1] = 95

# print(original)
# print(clone)
# # Because shallow copy does not copy nested objects; both containers still reference the same nested objects.
# print(original[0] is clone[0])

# # Deep Copy Recursively Duplicates Nested Objects
# from copy import deepcopy

# original = [["Sara", 90], ["Omar", 85]]
# clone = deepcopy(original)

# clone[0][1] = 95

# print(original)
# print(clone)
# # Deep copy creates an independent copy of the outer container and its nested mutable objects.
# print(original[0] is clone[0])

# # Choose the Lightest Correct Copy Strategy
# # Same object is okay
# alias = original

# # Only outer container needs independence
# clone = original.copy()

# # Nested mutable objects also need independence
# clone = deepcopy(original)

# # Operation Costs Matter Most Inside Repeated Work
# names = ["Sara", "Omar", "Lina"]
# print("Lina" in names)  # O(n): Because a list need to check items one by one.

# name_set = set(names)
# print("Lina" in name_set) # Average O(1): Sets use hashing to locate items without checking them one by one.

# # Build an Index When Records Need Repeated Lookup

# students = [
#     {"id": 101, "name": "Sara"},
#     {"id": 102, "name": "Omar"}
# ]
# students_by_id = {     # Build a dictionary index when records need repeated fast lookups by a key.
#     student["id"]: student
#     for student in students
# }
# print(students_by_id[102]["name"])

## Intermediate Python Fails When Intent Becomes Hidden:
## * Intermediate Python can become difficult to understand when too much logic is combined.
## * Code can be correct but still be unnecessarily complex.
## * Avoid forcing multiple operations into one complicated expression.
## * Separate complex operations when it makes the purpose of each step clearer.
## * Clear and readable code is better than clever but confusing code.

# # LAB 1 : normal loop vs list comprehension
# numbers = [1,2,3,4,5]
# squared_numbers = []

# for number in numbers:
#     squared_numbers.append(number ** 2)
# print(squared_numbers)

# comp_numbers = [ number ** 2 for number in numbers ]
# print(comp_numbers)

# # LAB 2: transformation + round()
# prices = [10,25,40]

# prices_with_vat = [
#     round(price * 1.15, 2)
#     for price in prices
# ]

# print(prices_with_vat)

# # LAB 3: string transformations in comprehensions

# names = ["SaRa", "ArEj", "Mashael", "nasser"]
# lower = [
#     name.lower()
#     for name in names
# ]
# upper = [
#     name.upper()
#     for name in names
# ]
# titled = [name.title() for name in names]

# print(lower, upper, titled)

# LAB 4: filtering + transformation

# c_temp = [20, 33, 15, 0]

# f_temp = [
#     (temp * 1.8 +32)
#     for temp in c_temp
#     if temp > 0
# ]
# print(f_temp)

# # LAB 5: flattening nested lists with multiple for clauses
# nested_list = [[1,2], [3,4],[5,6]]
# flattend_list = []
# for row in nested_list:
#     for column in row:
#         flattend_list.append(column)

# print(flattend_list)

# comp_flattened_list = [
#     column # A list comprehension automatically collects the expression results into a new list.
#     for row in nested_list
#     for column in row
# ]
# print(comp_flattened_list)

# # LAB 6: conditional expression in comprehension
# scores = [45, 55, 65, 75, 86, 95]
# passing_score = [
#     "Passed" if score >= 60 else "Failed"
#     for score in scores 
# ]
# print(passing_score)

# # LAB 7: set comprehension / removing duplicates
# skills = ["Python", "Git", "python", "Javascript", "SQL", "git"]

# skills_set= {
#     skill.lower()
#     for skill in skills
# }
# print(skills_set)

# # LAB 8: creating dictionaries inside a list comprehension

# list_name = ["Sara", "Dala", "Nouf", "Taif"]
# counted_chars = [
#     {"name":name, "count":len(name)}
#     for name in list_name 
# ]
# print(counted_chars)

# # LAB 9: generator expression + next() + generator exhaustion

# new_names = ["Mada", "Khadija", "Yamam", "Mashael"]

# upp = (
#     name.upper()
#     for name in new_names
# )

# print(next(upp))
# print(next(upp))
# print(list(upp))
# print("-"*5)
# for x in upp:
#     print(x)
