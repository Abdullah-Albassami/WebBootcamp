# Guided Practice

class Student:
    def __init__(self, name, scores= []):
        self.name = name
        self.scores = scores

    def average(self):
        if not self.scores:
            return 0
        return round(sum(self.scores) / len(self.scores), 2)

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)


class Course:
    def __init__(self, course, students=None):
        self.course = course
        self.students = [] if students is None else students

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def display(self):
        for student in self.students:
            return f"Name: {student.name}\nScores: {student.scores}\nAverage: {student.average()}"
            
# this is one way of creating instances:
# abdullah = Student("Abdullah", [96, 88])
# sara = Student("Sara", [96, 99])
# naser = Student("Naser", [96, 88])

course = Course("Python")
# Below is the required way by the instructor 
course.add_student(Student("Abdullah", [96, 88]))
course.add_student(Student("Sara", [96, 99]))
course.add_student(Student("Naser", [96, 88]))

print(course.display())



