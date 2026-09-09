# LAB 5
class Student:

    __enrolled = True

    def __init__(self, name, enrolled):
        self.name = name
        self.score = []
        self._enrolled = enrolled  # Stored the enrolled value in the object

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.score.append(score)

    # Getter
    @property  # Turned enrolled into a property
    def enrolled(self):
        return self._enrolled

    # Setter
    @enrolled.setter  # Added a setter to the enrolled property
    def enrolled(self, status):
        self._enrolled = status

    @property  # Made average accessible without ()
    def average(self):
        if not self.score:
            return 0
        else:
            return sum(self.score) / len(self.score)


student = Student("Khalifa", True)

student.add_score(80)
student.add_score(90)
student.add_score(100)

print(student.average)

student.enrolled = False  # Used the setter to change the enrollment status
print(student.enrolled)   # Used the getter to read the enrollment status

print(student.score)