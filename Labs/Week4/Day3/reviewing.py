from pathlib import Path

# # Task 1
# path = Path("data") / "students" / "scores.txt"
# print(path)
# print(path.name)
# print(path.suffix)

# # Task 2
# path = Path("data") / "students"
# path.mkdir(parents=True, exist_ok=True)
# print(path.exists())
# print(path.is_dir())

# # Task 3
# path = Path("data") / "students" / "names.txt"

# with path.open("x",  encoding="utf-8") as file:
#     file.write("Sara\nOmar")

# # Task 4
# path = Path("data") / "students" / "names.txt"

# with path.open("r", encoding="utf-8") as f:
#     print(f.read())

# # Task 5
# path = Path("data") / "students" / "names.txt"

# text = path.read_text(encoding="utf-8")
# print(text)

# # Task 6
# path = Path("data") / "students" / "names.txt"

# with path.open("r", encoding="utf-8") as f:
#     for line in f:
#         print(f"student: {line.strip()}")

# Task 7
path = Path("data") / "students" / "names.txt"

with path.open("w", encoding="utf-8") as f:
    f.write("Ali\nNorah")
    print(f)
