# 🐍 Week 04 Recap — Error Handling, Decorators & Modules

> Every production-grade Python program needs to handle errors gracefully, use decorators to extend behaviour cleanly, and be structured into reusable modules. This week was about making your code **robust, readable, and production-ready** — the same patterns used inside LangChain, FastAPI, and every serious AI framework.

---

## 🎯 Week Objective

Understand **how Python handles failure**, how **decorators** wrap and extend functions without changing them, and how **modules** let you organise code into reusable pieces with controlled entry points.

---

## ⏱️ Learning Summary

| Category   | Details                                                        |
| ---------- | -------------------------------------------------------------- |
| Duration   | ~12 Hours                                                      |
| Days       | Day 23 → Day 28                                                |
| Focus Area | Error Handling, Custom Exceptions, Decorators, Modules         |
| Main Goal  | Write robust, production-style Python programs                 |
| Milestone  | Task Manager CLI (Day 28)                                      |

---

## 📖 Concepts Covered

---

### 📌 Day 23 — Error Handling (`try / except / else / finally`)

> Gracefully handling runtime errors so your program doesn't crash unexpectedly.

```python
try:
    marks1 = int(input("Enter Python Marks: "))
    marks2 = int(input("Enter AI Marks: "))
    marks3 = int(input("Enter Math Marks: "))
    total   = marks1 + marks2 + marks3
    average = total / 3

except ValueError:
    print("Invalid input! Please enter only numbers for marks.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(f"Average : {average:.2f}")   # Runs only if no exception occurred

finally:
    print("Program execution completed.")  # Always runs
```

**Key Points:**
- `try` — block that might raise an exception
- `except` — catches a specific exception type; multiple `except` blocks are allowed
- `else` — runs **only** when the `try` block succeeds (no exception raised)
- `finally` — runs **always**, whether or not an exception occurred (use for cleanup)
- You can catch multiple exception types in one block: `except (ValueError, TypeError):`

**Block Execution Flow:**

| Scenario            | `try` | `except` | `else` | `finally` |
| ------------------- | :---: | :------: | :----: | :-------: |
| No exception        |  ✅   |    ❌    |   ✅   |    ✅     |
| Exception raised    |  ✅   |    ✅    |   ❌   |    ✅     |

---

### 📌 Day 24 — Custom Exceptions, `raise` & `assert`

> Defining your own exception classes and raising errors intentionally with business-rule validation.

```python
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass


try:
    age = int(input("Enter your age: "))

    assert age > 0, "Age must be greater than 0."   # assert for sanity checks

    if age < 18:
        raise InvalidAgeError("You must be at least 18 years old.")

except ValueError:
    print("Please enter a valid number.")

except AssertionError as error:
    print(error)

except InvalidAgeError as error:
    print(error)
```

**Key Points:**
- **Custom exceptions** inherit from `Exception` (or any built-in exception)
- `raise ExceptionClass("message")` — manually trigger an exception
- `assert condition, "message"` — raises `AssertionError` if condition is `False`; used for debugging / sanity checks
- Use custom exceptions to communicate **domain-specific errors** clearly (e.g., `InvalidAgeError` vs a generic `ValueError`)
- Catch custom exceptions just like built-in ones: `except InvalidAgeError as error:`

**When to use each:**

| Tool             | Use Case                                              |
| ---------------- | ----------------------------------------------------- |
| `raise`          | Enforce business rules (age, score range, etc.)       |
| `assert`         | Sanity checks during development / testing            |
| Custom Exception | Give meaningful names to domain-specific error states |

---

### 📌 Day 25 — Basic Decorators

> A decorator is a function that **wraps another function** to add behaviour before and/or after it runs — without modifying the original function.

```python
def welcome_decorator(function):

    def wrapper():
        print("=" * 40)
        print("Welcome to the Student Portal")
        print("=" * 40)

        function()                         # Call the original function

        print("=" * 40)
        print("Program Completed Successfully")
        print("=" * 40)

    return wrapper                         # Return the wrapper, not the result


@welcome_decorator                         # Syntactic sugar — same as:
def display_student():                     # display_student = welcome_decorator(display_student)
    name   = input("Enter Student Name: ")
    course = input("Enter Course Name: ")
    print(f"Name   : {name}")
    print(f"Course : {course}")


display_student()
```

**Key Points:**
- A decorator is a **higher-order function** — it takes a function and returns a new function
- `@decorator_name` is syntactic sugar for `func = decorator_name(func)`
- The inner `wrapper` function is what actually gets called when you call the decorated function
- The original function is called **inside** the wrapper at the right point

**Anatomy of a Decorator:**
```
decorator(function)
    └── wrapper()           ← what the caller actually calls
          ├── before logic
          ├── function()    ← original function runs here
          └── after logic
```

---

### 📌 Day 26 — Advanced Decorators (`*args`, `**kwargs`, `@wraps`, stacking)

> Making decorators flexible enough to work on any function and stacking multiple decorators.

```python
from functools import wraps


def logger(function):

    @wraps(function)                       # Preserves original function metadata
    def wrapper(*args, **kwargs):
        print("Starting function...")
        result = function(*args, **kwargs) # Pass through all arguments
        print("Function completed.")
        return result

    return wrapper


def divider(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("=" * 40)
        result = function(*args, **kwargs)
        print("=" * 40)
        return result

    return wrapper


@divider
@logger                                    # Stacked — divider wraps logger wraps the function
def student_details():
    name   = input("Enter Student Name: ")
    course = input("Enter Course: ")
    print(f"Name   : {name}")
    print(f"Course : {course}")


student_details()
```

**Key Points:**
- `*args, **kwargs` — allows the decorator's wrapper to accept **any** arguments and pass them through
- `@functools.wraps(function)` — copies the original function's `__name__`, `__doc__` etc. to the wrapper (important for debugging & introspection)
- **Decorator stacking**: `@divider` applied after `@logger` means execution order is outer → inner → function → inner → outer
- Always `return result` from the wrapper so the decorated function's return value is not lost

**Stacking execution order:**
```
@divider
@logger
def student_details(): ...

# Equivalent to:
student_details = divider(logger(student_details))

# Call order: divider → logger → student_details → logger → divider
```

---

### 📌 Day 27 — Modules & `__main__`

> Organising code into reusable modules and using `__name__ == "__main__"` to control script entry points.

```python
from math import sqrt
import math


def calculate_square_root():
    number = float(input("Enter a number: "))
    print(f"Square Root: {sqrt(number)}")


def calculate_power():
    base     = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    print(f"Result: {math.pow(base, exponent)}")


def calculate_factorial():
    number = int(input("Enter a positive integer: "))
    print(f"Factorial: {math.factorial(number)}")


def main():
    while True:
        choice = input("Choose an option (1-4): ")
        if   choice == "1": calculate_square_root()
        elif choice == "2": calculate_power()
        elif choice == "3": calculate_factorial()
        elif choice == "4": break
        else: print("Invalid Choice!")


if __name__ == "__main__":
    main()
```

**Key Points:**
- `import math` — imports the whole module; access with `math.sqrt()`
- `from math import sqrt` — imports a specific name; access directly as `sqrt()`
- `__name__` is a special variable Python sets automatically:
  - `"__main__"` — when the file is **run directly**
  - `"module_name"` — when the file is **imported** by another file
- `if __name__ == "__main__": main()` — the standard Python entry-point pattern; prevents code from running on import

**Import comparison:**

| Style                      | Usage         | Example                        |
| -------------------------- | ------------- | ------------------------------ |
| `import math`              | Full module   | `math.sqrt(16)`                |
| `from math import sqrt`    | Specific name | `sqrt(16)`                     |
| `from math import *`       | Everything    | Avoid — pollutes namespace     |
| `import math as m`         | Alias         | `m.sqrt(16)`                   |

---

### 📌 Day 28 — Week 04 Milestone: Task Manager CLI

> Applied error handling, modules, `__main__`, and list operations in a complete CLI project.

```python
tasks = []


def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def remove_task():
    view_tasks()
    if not tasks:
        return
    task_number = int(input("\nEnter task number to remove: "))
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"{removed} removed successfully.")
    else:
        print("Invalid task number.")


def main():
    while True:
        choice = input("Choose an option (1-4): ")
        if   choice == "1": add_task()
        elif choice == "2": view_tasks()
        elif choice == "3": remove_task()
        elif choice == "4": break
        else: print("Invalid choice.")


if __name__ == "__main__":
    main()
```

**Concepts Applied:**
- ✅ Functions organised into single-responsibility units
- ✅ `if __name__ == "__main__"` entry-point pattern
- ✅ List operations: `append()`, `pop()`, `enumerate()`
- ✅ Input validation with bounds checking
- ✅ While loop menu pattern

---

## 🛠️ Projects Built This Week

| # | Project                    | Concepts Applied                                                  |
|---|----------------------------|-------------------------------------------------------------------|
| 1 | Student Marks Calculator   | `try/except/else/finally`, `ValueError`, `ZeroDivisionError`      |
| 2 | Age Registration System    | Custom exceptions, `raise`, `assert`, `AssertionError`            |
| 3 | Student Portal Decorator   | Basic decorators, `@syntax`, wrapper pattern                      |
| 4 | Student Info Logger        | Advanced decorators, `*args/**kwargs`, `@wraps`, decorator stacking|
| 5 | Simple Math Tool           | `import math`, `from math import`, `__main__` entry point         |
| 6 | Task Manager CLI           | Full CLI project — functions, lists, `__main__`, input validation  |

---

## 🌍 Real-World Relevance

| What You'll See in AI / Production Code         | Python Pattern Used This Week              |
| ----------------------------------------------- | ------------------------------------------ |
| `try/except` around API calls and I/O           | Error Handling (Day 23)                    |
| `raise ValueError("Invalid token")` in SDKs     | `raise` & Custom Exceptions (Day 24)       |
| `@app.route(...)` in Flask / FastAPI            | Decorators (Day 25–26)                     |
| `@torch.no_grad()` in PyTorch                   | Advanced Decorators (Day 26)               |
| `if __name__ == "__main__":` in every script    | Modules & Entry Points (Day 27)            |
| CLI tools like LangChain, Hugging Face CLI      | Task Manager pattern (Day 28)              |

---

## 📚 Resources Used

- **Python Docs — Errors and Exceptions** — docs.python.org/3/tutorial/errors.html
- **Python Docs — functools.wraps** — docs.python.org/3/library/functools.html#functools.wraps
- **Real Python — Primer on Decorators** — realpython.com/primer-on-python-decorators
- **Real Python — Python Modules and Packages** — realpython.com/python-modules-packages
- **Corey Schafer — Decorators** — youtube.com/@coreyms
- **Python for Everybody** — py4e.com (Chapters on Functions & Modules)

---

## 🧠 Self-Check Questions

1. **What is the difference between `except` and `else`** in a `try` block? When does `else` run?
2. **Why do we use `finally`?** Give a real-world example of when you'd need it.
3. **What is a custom exception?** Write one called `InsufficientFundsError`.
4. **What does `@wraps(function)` do** and why is it important?
5. **Explain decorator stacking.** If `@A` and `@B` are applied to `func`, in what order do they execute?
6. **What is `__name__`?** What value does it hold when a file is run directly vs imported?
7. **Rewrite the Task Manager** to save tasks to a `.txt` file so they persist between runs.

---

## ✅ Week 04 Completion Status

- [x] Day 23 — Error Handling (`try / except / else / finally`)
- [x] Day 24 — Custom Exceptions, `raise` & `assert`
- [x] Day 25 — Basic Decorators
- [x] Day 26 — Advanced Decorators (`*args`, `**kwargs`, `@wraps`, stacking)
- [x] Day 27 — Modules & `__main__`
- [x] Day 28 — Week Milestone: Task Manager CLI

---

*Next week → File I/O, JSON handling, virtual environments, and packaging Python projects.*
