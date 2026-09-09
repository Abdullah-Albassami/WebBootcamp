# # WEEK 3 DAY 4

# # A comperhansions combines an experssion, loop and filter

# numbers = [1, 2, 3, 4, 5 ]

# squares = [ number ** 2 for number in numbers if number % 2 == 1 ]

# print(squares) 

# # List comperhensions transform every item

# prices = [10, 25, 40]

# prices_with_vat = [ 
#     round(price * 1.15, 2)
#     for price in prices # in comperhansion, iteration is mandutory
# ]
# print(prices_with_vat)

# # A filter keeps only that match a condtion 

# scores = [42, 67, 91, 58, 75]

# passing_scores = [ score for score in scores if score >= 60 ]

# print(passing_scores)

# # Filtering and Transformation Can Work Together

# raw_names = [" sara ", "", "OMAR", "lina"]
# clean_name = [
#     name.strip().title()
#     for name in raw_names
#     if name.strip()
# ]
# # print(clean_name)
# for name in raw_names:
#     name.strip()
#     print(name)

# # multiple for clauses follow nested-loop order
# numbers = [1, 2]
# letters = ["A", "B"]
# pairs = [
#     (number, letter)
#     for number in numbers
#     for letter in letters
# ]
# print(pairs)
# # A condition Expression prduces one of two values
# scores = [42, 67, 91]

# labels = [ 
#     "pass" if score >= 60 else "retry"
#     for score in scores
# ]
# print(labels)

# # A set comperhansion removes duplicate results

# emails = [ 
#     "SARA@EXAMPLE.COM",
#     "omar@example.com",
#     "lina@school.sa"
# ]

# domains = {
#     email.split("@")[1].lower() # foucs on split ((important))
#     for email in emails
# }
# print(domains)

# Dictionary comperhansions build mappings

# numbers = range(1, 6)
# squares = {
#     number: number ** 2
#     for number in numbers
# }
# print(squares)
# task reasearch creating a dict inside a tuple and modfy it

# tup = ("A", 66, {"Brand": "Toyota", "Name": "RAV-4", "Year": 2025})

# tup[2]["Name"] = "Camry"

# print(tup)
