# # Exercise 1
# def yourName(name):
#     for char in name:
#         print(char)

# yourName("Naser")

# Exercise 2

students = [
    {"name": "Ahmed", "scores": (70, 80, 99), "skills": {"coding", "Typing", "Hacking", "art"}},
    {"name": "Sara", "scores": (75, 83, 91), "skills": {"Painting", "designing", "writing", "art"}},
    {"name": "Rami", "scores": (76, 87, 90), "skills": {"reading", "speaking", "listing", "art"}},
]

for s in students:
    total = 0
    all_skills = set()
    for score in s["scores"]:
        total += score
    avrg = total / len(s["scores"])
    
    s["skills"].add("eating")
    s["skills"].add("eating")
    all_skills = all_skills | s["skills"]
    print(f"{s["name"]}: {avrg:.0f}, Skills: {s["skills"]}")



print(f"All Uniqe skills: {all_skills}")




