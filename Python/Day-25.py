# ==========================================
# DAY 25 — BASIC DECORATORS
# ==========================================


def welcome_decorator(function):

    def wrapper():
        print("=" * 40)
        print("Welcome to the Student Portal")
        print("=" * 40)

        function()

        print("=" * 40)
        print("Program Completed Successfully")
        print("=" * 40)

    return wrapper


@welcome_decorator
def display_student():

    name = input("Enter Student Name: ")
    course = input("Enter Course Name: ")

    print("\n===== STUDENT DETAILS =====")
    print(f"Name   : {name}")
    print(f"Course : {course}")


display_student()
