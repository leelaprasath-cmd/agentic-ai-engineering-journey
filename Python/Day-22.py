# ==========================================
# WEEK 03 MILESTONE PROJECT
# STUDENT MANAGEMENT SYSTEM
# ==========================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):

    school = "AI Engineering Academy"

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    # Instance Method
    def student_details(self):
        print("\n===== STUDENT DETAILS =====")
        self.introduction()
        print(f"Course : {self.course}")
        print(f"School : {Student.school}")

    # Method Overriding
    def introduction(self):
        print(f"Student Name : {self.name}")
        print(f"Age          : {self.age}")

    # Class Method
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # Static Method
    @staticmethod
    def welcome():
        print("===== STUDENT MANAGEMENT SYSTEM =====")

    # Dunder Methods
    def __str__(self):
        return f"{self.name} - {self.course}"

    def __repr__(self):
        return f"Student('{self.name}', {self.age}, '{self.course}')"

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        return self.age == other.age


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

Student.welcome()

Student.change_school("Agentic AI Institute")

student1 = Student("Leela", 19, "AI Engineering")
student2 = Student("Hemanth", 19, "Computer Science")

student1.student_details()
student2.student_details()

print("\n===== DUNDER METHODS =====")
print(student1)
print(repr(student1))
print("Length of Name:", len(student1))
print("Same Age:", student1 == student2)

print("\n===== isinstance() =====")
print(isinstance(student1, Student))
print(isinstance(student1, Person))
print(isinstance(student2, Person))
