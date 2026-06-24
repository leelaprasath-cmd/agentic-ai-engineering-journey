# ==========================================
# DAY 15 — CLASSES AND OBJECTS
# ==========================================

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course



student1 = Student("Leela", 19, "AI Engineering")
student2 = Student("Hemanth", 20, "Computer Science")


print("===== STUDENT DETAILS =====")

print("\nStudent 1")
print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)

print("\nStudent 2")
print("Name:", student2.name)
print("Age:", student2.age)
print("Course:", student2.course)
