# Guided Practice:

# 1. Create a list of student dictionaries, each containing a name and a nested list of scores.
# 2. Use a list comprehension to calculate each student's average.
# 3. Filter the report to keep students whose average is ≥ 60.
# 4. Build a dictionary index mapping each student's name → their report record.
# 5. Use deepcopy() to create an independent backup, then modify nested data to prove the original and backup don't affect each other.

students = [
    {"name": "sara", "scores": [71, 86, 97]},
    {"name": "ahmed", "scores": [45, 30, 60]},
    {"name": "omar", "scores": [59, 88, 85]}
]


student_report = [
    {
        "name": student["name"],
        "scores": student["scores"],
        "avrg": round(sum(student["scores"]) / len(student["scores"]), 2)
    }
    for student in students
]

passed_student = {
    student["name"]: student
    for student in student_report
    if student["avrg"] >= 60
}
from copy import deepcopy

clone = deepcopy(student_report)
clone[0]["scores"][1] = 95

print(student_report[0]["scores"][1])
print(clone[0]["scores"][1])

# print(student_report)
# print(passed_student)


# Indvidual Practice: (Multiple Tasks)

# Task 1 — Easy
# prices = [10, 25, 40, 55, 80]

# prices_with_vat = [ round(price * 1.15, 2) for price in prices ]

# expensive_prices = [ price for price in prices if price >= 40 ]

# labels = [ "cheap" if price < 40 else "expensive" for price in prices ] 

# print(prices)
# print(prices_with_vat)
# print(expensive_prices)
# print(labels)

# # Task 2 — Medium

# products = [
#     {"name": " laptop ", "price": 3500, "category": "Electronics", "tags": ["Tech", "Portable"]},
#     {"name": "MOUSE", "price": 120, "category": "Electronics", "tags": ["Tech", "Accessory"]},
#     {"name": " desk ", "price": 850, "category": "Furniture", "tags": ["Office", "Wood"]},
#     {"name": "CHAIR", "price": 450, "category": "Furniture", "tags": ["Office", "Comfort"]},
#     {"name": " monitor ", "price": 1200, "category": "Electronics", "tags": ["Tech", "Display"]}
# ]
# clean_names = [ product["name"].strip().title() for product in products ]

# affordable_products = [ product for product in products if product["price"] <= 1000 ]

# price_labels = [ "Budget" if product["price"] < 500 else "Premium" for product in products ]

# unique_tags = { tag.lower()for product in products for tag in product["tags"] }

# product_prices = { product["name"].strip().title(): round(product["price"] * 1.15, 2) for product in products }

# print("clean_names: \n",clean_names)
# print("affordable_products: \n",affordable_products)
# print("price_labels: \n",price_labels)
# print("unique_tags: \n",unique_tags)
# print("product_prices: \n",product_prices)

# # Task 2 - Hard Task

# courses = [
#     {
#         "name": " python ",
#         "students": ["Sara", "Omar", "Lina"],
#         "scores": [85, 52, 91],
#         "tags": ["Programming", "Backend"]
#     },
#     {
#         "name": "DJANGO",
#         "students": ["Ahmed", "Sara"],
#         "scores": [78, 88],
#         "tags": ["Web", "Backend"]
#     },
#     {
#         "name": " html ",
#         "students": ["Omar", "Lina", "Ahmed"],
#         "scores": [90, 95, 91],
#         "tags": ["Web", "Frontend"]
#     }
# ]

# clean_course_names = [ course["name"].strip().title() for course in courses ]

# score_labels = [ "Pass" if score >= 60 else "Retry" for course in courses for score in course["scores"] ]

# unique_tags = { tag.lower().title() for course in courses for tag in course["tags"] }

# course_averages = { course["name"].strip().title(): round(sum(course["scores"]) / len(course["scores"]), 2) for course in courses }

# passing_scores = [ score for course in courses for score in course["scores"] if score >= 60 ]

# # print(clean_course_names)
# # print(score_labels)
# # print(unique_tags)
# # print(course_averages)
# # print(passing_scores)
# # high_score_courses — a list containing the entire course dictionary only for courses that have at least one score of 90 or higher.

# high_score_courses = [ 
#     course
#     for course in courses 
#     for score in course["scores"]
#     if score >= 90 

# ]
# print(high_score_courses)
