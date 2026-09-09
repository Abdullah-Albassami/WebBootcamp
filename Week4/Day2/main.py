# class Dog:
#     _legs = 4

#     def __init__(self, name):
#         self.name = name

#     def getLegs(self):
#         return Dog._legs

#     def setLegs(self, number):
#         self._legs = number

#     def talk(self, sound):
#         self.sound = sound
#         return (f"{self.name} says: {sound}!")

# dog1 = Dog("Peter")
# print(dog1.talk("hello"))
# print(dog1.sound)

# # Week 4 Day2: ==> File Handling & Exception Managment

# # Files Make Program State Last beyond One Run

# # Pasth Objects build locations Portably
# from pathlib import Path

# data_file = Path("data") / "students.txt"

# print(data_file)
# print(data_file.name)
# print(data_file.suffix)

# # Inspect Path before using them
# from pathlib import Path

# data_dir = Path("data")
# data_dir.mkdir(exist_ok=True)

# data_file = data_dir / "students.txt"

# print(data_dir.is_dir())
# print(data_file.exists())

# File mode Decide What may change
# "r" read existing file
# "w" write and replace content
# "a" append after existing content
# "x" create only when absent

# with open ("notes.txt", "x", encoding="utf-8") as file:
#     file.write("New note\n")

# #  with closes the file automatically
# from pathlib import Path
# path = Path("notes.txt")

# with path.open("r", encoding="utf-8") as file:
#     content = file.read()

# print(content)
# print(file.closed) # True

# # Read complete text when the file is small
# from pathlib import Path

# path = Path("notes.txt")
# with path.open("r", encoding="utf-8") as file:
#     text = file.read()

# same_text = path.read_text(encoding="utf-8")

# print(text == same_text)

# # itrate over lines without loading everything
# from pathlib import Path
# path = Path("students.txt")
# with path.open("r", encoding="utf-8") as file:
#     for line in file:
#         name = line.strip()
#         if name:
#             print(name)

# # writing replaces existion content
# from pathlib import Path
# path = Path("students.txt")
# with path.open("w", encoding="utf-8") as file:
#     count = file.write("Sara\nAli\n")

# print(count)

# # Appending presserves existing content
# from pathlib import Path
# path = Path("activity.log")

# with path.open("a", encoding="utf-8") as file:
#     file.write("student enrolled: Sara\n")
#     print("Activity saved")

# # UTF-8 and newline keeps text predictable
# from pathlib import Path
# names = ["Sara", "نورة", "Ali"]
# text = "\n".join(names) + "\n"

# Path("students.txt").write_text(
#     text,
#     encoding="utf-8"
# )
