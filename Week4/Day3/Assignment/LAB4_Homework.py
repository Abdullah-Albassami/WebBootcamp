# LAB 4
from pathlib import Path

path = Path("home") / "students" / "students.txt" 

path.parent.mkdir(parents=True, exist_ok=True)

print(path.is_dir())
print(path.suffix)
print(path.name)
print(path.is_file())

path.write_text("Welcome to class", encoding="utf-8")