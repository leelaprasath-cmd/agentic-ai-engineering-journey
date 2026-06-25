# ==========================================
# DAY 17 — CLASS METHODS & STATIC METHODS
# ==========================================

class Student:

    school = "AI Engineering Academy"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def welcome_message():
        print("Welcome to the Student Management System")


Student.welcome_message()

Student.change_school("Agentic AI Institute")

student1 = Student("Leela")
student2 = Student("Hemanth")

print("\nStudent 1:", student1.name)
print("School:", student1.school)

print("\nStudent 2:", student2.name)
print("School:", student2.school)
