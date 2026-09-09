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






#######################################################################
# Guided Practice my version
# class Student:
#     def __init__(self, name, scores = []):
#         self.name = name
#         self.scores = scores

#     def add_score(self):
#         if 0 <= self.value <= 100:
#             return self.scores.append(self.value)
#         return False

#     def avrg(self):
#         if not self.vale:
#             return 0

#         return sum(self.scores) /len(self.scores)

# student = Student("Abdullah", [90, 91, 89])

# student.add_score = 100

# print(student.avrg())

#######################################################################

# class Student:
#     def __init__(self, name, scores = []):
#         self.name = name
#         self.scores = scores

#     def average(self):
#         if not self.scores:
#             return 0
#         return round(sum(self.scores) / len(self.scores), 2)
#     def add_score(self, score):
#         if 0 <= score <= 100:
#             self.scores.append(score)
# class Course:
#     def __init__(self, course, students=[]):
#         self.course = course
#         self.students = students
#     if isinstance(Student):
#     # def display(self):
#     #     return f"Course name: {self.course}\n Student Info: {self.student}"

# Abdullah = Student("Abdullah", [96, 88])
# Abdullah.add_score("Sara", [96, 99])
# Abdullah.a("Naser", [96, 88])

# course = Course("Python", Abdullah)


# print(course.display())
    


