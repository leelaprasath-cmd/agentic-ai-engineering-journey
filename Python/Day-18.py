# ==========================================
# DAY 18 — DUNDER METHODS
# ==========================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # String Representation
    def __str__(self):
        return f"Student(Name={self.name}, Age={self.age})"

    # Official Representation
    def __repr__(self):
        return f"Student('{self.name}', {self.age})"

    # Length Method
    def __len__(self):
        return len(self.name)

    # Equality Method
    def __eq__(self, other):
        return self.age == other.age


student1 = Student("Leela", 19)
student2 = Student("Hemanth", 19)

print("Using __str__():")
print(student1)

print("\nUsing __repr__():")
print(repr(student1))

print("\nUsing __len__():")
print(len(student1))

print("\nUsing __eq__():")
print(student1 == student2)
