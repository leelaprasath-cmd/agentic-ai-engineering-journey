# ==========================================
# DAY 26 — ADVANCED DECORATORS
# ==========================================

from functools import wraps


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Starting function...")
        result = function(*args, **kwargs)
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
@logger
def student_details():

    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    print("\nStudent Information")
    print(f"Name   : {name}")
    print(f"Course : {course}")


student_details()
