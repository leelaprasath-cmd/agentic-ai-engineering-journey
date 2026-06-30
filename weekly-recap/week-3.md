# 🐍 Week 03 Recap — Python OOP: Classes, Objects & Inheritance

> Every AI framework you will use — PyTorch, LangChain, LlamaIndex — is built with OOP. When you write `model = LinearRegression()` or `agent = Agent(tools=[...])` — you are using OOP. This week was about understanding what is happening under the hood.

---

## 🎯 Week Objective

Understand **why OOP exists** — it is about organizing code into reusable, modular pieces. Focus on `__init__`, `self`, and inheritance — not just the syntax, but the design pattern behind it.

---

## ⏱️ Learning Summary

| Category   | Details                                         |
| ---------- | ----------------------------------------------- |
| Duration   | ~14 Hours                                       |
| Days       | Day 15 → Day 22                                 |
| Focus Area | Object-Oriented Programming                     |
| Main Goal  | Master Classes, Methods, Inheritance & OOP Mini Projects |
| Milestone  | Student Management System (Day 22)              |

---

## 📖 Concepts Covered

---

### 📌 Day 15 — Classes and Objects

> `class` keyword, `__init__`, `self`, attributes, creating instances.

```python
class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Leela", 19, "AI Engineering")
```

**Key Points:**
- A **class** is a blueprint; an **object** is an instance of that blueprint
- `__init__` is the constructor — runs automatically when an object is created
- `self` refers to the current instance of the class
- **Instance attributes** are unique to each object

---

### 📌 Day 16 — Instance Methods

> Methods that operate on instance data using `self`.

```python
class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
```

**Key Points:**
- Instance methods always take `self` as the first parameter
- They can read and modify instance attributes
- Called on an object: `student1.display_details()`

---

### 📌 Day 17 — Class Methods & Static Methods

> `@classmethod` operates on the class itself. `@staticmethod` is a utility that doesn't need `self` or `cls`.

```python
class Student:

    school = "AI Engineering Academy"   # Class attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school         # Modifies class-level data

    @staticmethod
    def greet():
        print("Welcome to AI Engineering Academy!")
```

| Method Type     | First Parameter | Access               |
| --------------- | --------------- | -------------------- |
| Instance Method | `self`          | Instance + Class data |
| Class Method    | `cls`           | Class data only       |
| Static Method   | None            | No class/instance data |

---

### 📌 Day 18 — Dunder (Magic) Methods

> Special methods that make your objects behave naturally with Python's built-in operations.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(Name={self.name}, Age={self.age})"

    def __repr__(self):
        return f"Student('{self.name}', {self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
```

**Dunder Methods Covered:**

| Method     | Purpose                                   |
| ---------- | ----------------------------------------- |
| `__init__` | Constructor — initialize attributes       |
| `__str__`  | Human-readable string (`print()`, `str()`) |
| `__repr__` | Official representation (`repr()`)        |
| `__len__`  | Called by `len()`                         |
| `__eq__`   | Called by `==` operator                   |

**`__str__` vs `__repr__`:**
- `__str__` → for end users (readable)
- `__repr__` → for developers (unambiguous, should ideally recreate the object)

---

### 📌 Day 19 — Inheritance

> Child classes inherit attributes and methods from a parent class.

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name :", self.name)
        print("Age  :", self.age)


class Student(Person):             # Student inherits from Person

    def __init__(self, name, age, course):
        super().__init__(name, age)    # Call parent constructor
        self.course = course

    def display_student(self):
        self.display_person()          # Reusing parent method
        print("Course :", self.course)
```

**Key Points:**
- `super().__init__()` calls the parent class constructor — avoids rewriting code
- Child class has access to all parent methods and attributes
- Promotes **code reuse** and **hierarchical design**

---

### 📌 Day 20 — Method Overriding & `isinstance()`

> Child classes can override parent methods to provide their own behavior.

```python
class Person:

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print(f"My name is {self.name}.")


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduction(self):              # Overrides parent method
        print(f"My name is {self.name} and I study {self.course}.")
```

**`isinstance()` Check:**
```python
s = Student("Leela", "AI Engineering")
print(isinstance(s, Student))   # True
print(isinstance(s, Person))    # True — Student IS-A Person
```

---

### 📌 Day 21 — OOP Mini Project: Library Management System

> Applied all OOP concepts in a real mini-project.

```python
class Book:

    library_name = "AI Engineering Library"

    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def display_book(self):
        status = "Available" if self.available else "Issued"
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")

    def issue_book(self):
        if self.available:
            self.available = False
            print(f"'{self.title}' has been issued.")
        else:
            print(f"'{self.title}' is already issued.")

    def return_book(self):
        self.available = True
        print(f"'{self.title}' has been returned.")
```

**OOP Concepts Used in This Project:**
- ✅ Class attributes (`library_name`)
- ✅ Instance attributes (`title`, `author`, `available`)
- ✅ Instance methods (`display_book`, `issue_book`, `return_book`)
- ✅ Conditional logic inside methods

---

### 📌 Day 22 — Week 03 Milestone: Student Management System

> Full OOP application combining **Inheritance + Class Methods + Instance Methods + Method Overriding**.

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):

    school = "AI Engineering Academy"   # Class attribute

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def student_details(self):          # Instance method
        print("\n===== STUDENT DETAILS =====")
        self.introduction()
        print(f"Course : {self.course}")

    @classmethod
    def change_school(cls, new_school): # Class method
        cls.school = new_school

    @staticmethod
    def school_info():                  # Static method
        print("School : AI Engineering Academy")

    def introduction(self):             # Method overriding
        super().introduction()
        print(f"Course : {self.course}")
```

---

## 🛠️ Projects Built This Week

| # | Project                    | Concepts Applied                                      |
|---|----------------------------|-------------------------------------------------------|
| 1 | Library Management System  | Class attributes, instance methods, book state logic  |
| 2 | Student Management System  | Full inheritance, class/instance/static methods, override |

---

## 🌍 Real-World Relevance

| What You'll Write in AI          | OOP Concept Used This Week           |
| -------------------------------- | ------------------------------------ |
| `model = LinearRegression()`     | Classes & Objects (Day 15–16)        |
| `class MyModel(nn.Module):`      | Inheritance (Day 19–20)              |
| `class MyAgent(Agent):`          | Method Overriding + `super()`        |
| `class CustomTool(BaseTool):`    | Child classes inheriting behavior    |

---

## 📚 Resources Used

- **Corey Schafer OOP Python Series** — youtube.com/@coreyms
- **Python for Everybody** — Chapter 14 (py4e.com)
- **Real Python OOP Guide** — realpython.com/python3-object-oriented-programming
- **Python Docs** — docs.python.org/3/tutorial/classes.html
- **Fluent Python** — Chapters 1–2 by Luciano Ramalho
- **Practice:** Exercism Python OOP track — exercism.org/tracks/python

---

## 🧠 Self-Check Questions

1. **What is the difference between a class attribute and an instance attribute?** Give an example.
2. **Why do we pass `self` as the first parameter** to every instance method?
3. **What does `super().__init__()` do?** Why do we call it in a child class?
4. **Explain method overriding** with a simple example.
5. **What is the difference between `__str__` and `__repr__`?** When is each called?
6. **Can a child class access private attributes (`__x`) of a parent?** What about protected (`_x`)?
7. **Write a `Shape` base class** with an `area()` method. Create `Circle` and `Rectangle` subclasses.

---

## ✅ Week 03 Completion Status

- [x] Day 15 — Classes and Objects
- [x] Day 16 — Instance Methods
- [x] Day 17 — Class Methods & Static Methods
- [x] Day 18 — Dunder Methods (`__str__`, `__repr__`, `__eq__`)
- [x] Day 19 — Inheritance & `super()`
- [x] Day 20 — Method Overriding & `isinstance()`
- [x] Day 21 — OOP Mini Project: Library Management System
- [x] Day 22 — Week Milestone: Student Management System

---

*Next week → Error Handling, Custom Exceptions, Decorators, and advanced Python patterns.*
