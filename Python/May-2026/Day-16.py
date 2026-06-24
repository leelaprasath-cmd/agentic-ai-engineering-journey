# ==========================================
# DAY 16 — INSTANCE METHODS
# ==========================================

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("\n===== STUDENT DETAILS =====")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def study(self):
        print(f"{self.name} is studying {self.course}.")



student1 = Student("Leela", 19, "AI Engineering")
student2 = Student("Hemanth", 20, "Computer Science")



student1.display_details()
student1.study()

student2.display_details()
student2.study()
