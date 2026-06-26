# ==========================================
# DAY 20 — METHOD OVERRIDING & isinstance()
# ==========================================

class Person:

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print(f"My name is {self.name}.")


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduction(self):
        print(f"My name is {self.name} and I study {self.course}.")


person = Person("Rahul")
student = Student("Leela", "AI Engineering")

print("===== METHOD OVERRIDING =====")
person.introduction()
student.introduction()

print("\n===== isinstance() =====")
print(isinstance(person, Person))
print(isinstance(student, Student))
print(isinstance(student, Person))
