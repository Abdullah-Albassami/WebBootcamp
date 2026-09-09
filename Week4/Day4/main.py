# # LAB 5
# #Name-Mangling
# #Property

# class Student:

#     __enrolled = True

#     def __init__(self, name,enrolled):
#         self.name = name
#         self.score = []

#     def add_score(self, score):
#         if score < 0 or score >100:
#             raise ValueError("Score must be between 0 and 100")
#         self.score.append(score)

#     #Getter
#     def enrolled(self):
#         return self._enrolled

#     #Setter
#     @enrolled.setter
#     def enrolled(self, status):
#         self._enrolled = status

#     @property
#     def average(self):
#         if not self.score:
#             return 0
#         else:
#             return sum(self.score) / len(self.score)


# student = Student("Khalifa", None)
# student.add_score(80)
# student.add_score(90)
# student.add_score(100)

# print(student.average)

# student.setEnrolled(False)
# student.enrolled = True
# print(student.getEnrollment())
# print(student.score)

# # LAB 6
# class Food:
#     def __init__(self, name):
#         self.name = name
#     def showName(self):
#         return self.name

# class Fruits(Food):
#     newName = "  Fa  "
#     def __init__(self, name, cal):
#         super().__init__(name)
#         self.cal = cal
#     @staticmethod    
#     def stripName(newName):
#         return newName.strip()

# apple = Fruits("Apple", 200)
# print(apple.showName())
# print(apple.stripName("  Fa  "))