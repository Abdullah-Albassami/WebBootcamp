# class Student:
#     def __init__(self, name, scores = []):
#         self.name = name
#         self.scores = scores

#     def add_score(self, score):
#         if 0 > score or score > 100:
#             return False
#         self.scores.append(score)

#     def avrage(self):
#         if not self.scores:
#             return 0

#         return sum(self.scores) / len(self.scores)

# class Course:
#     def __init__(self, c_name, students= []):
#         self.c_name = c_name
#         self.student = students

#     def add_student(self, student):        
#         if isinstance(student, Student):
#             self.student.append(student)
#         else:
#             return False

#     def display(self):
#         for student in students:
#             return f"Course name: {self.c_name} Student name: {self.Student.name}, Student Scores: {self.Student.scores}, Avrage: {self.Student.avrage()}"



# student = Student("Abdullah", [85, 96])
# student.add_score(100)

# course1 = Course(student, "Python")


# print(course1.display())



