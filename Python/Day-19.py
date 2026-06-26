# ==========================================
# DAY 19 — INHERITANCE
# ==========================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name :", self.name)
        print("Age  :", self.age)


class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        self.display_person()
        print("Course :", self.course)


student1 = Student("Leela Prasath", 19, "AI Engineering")

print("===== STUDENT DETAILS =====")
student1.display_student()
