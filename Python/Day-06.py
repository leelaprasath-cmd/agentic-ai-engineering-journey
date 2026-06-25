# ==========================================
# DAY 06 — FUNCTIONS & SCOPE
# ==========================================


print("========== FUNCTIONS IN PYTHON ==========")


def welcome_message():
    print("Welcome to Python Functions")

welcome_message()



print("\n========== FUNCTION WITH PARAMETERS ==========")

def student_details(name, department):
    print("Student Name :", name)
    print("Department   :", department)

student_details("Leela Prasath", "CSE")



print("\n========== FUNCTION WITH RETURN ==========")

def add_numbers(a, b):

    result = a + b

    return result

sum_result = add_numbers(10, 20)

print("Addition Result :", sum_result)



print("\n========== DEFAULT ARGUMENT ==========")

def course_details(course_name="Python"):

    print("Current Course :", course_name)

course_details()

course_details("Artificial Intelligence")


print("\n========== VARIABLE SCOPE ==========")

global_variable = "I am Global"

def scope_demo():

    local_variable = "I am Local"

    print(global_variable)
    print(local_variable)

scope_demo()

print(global_variable)



print("\n========== USER INPUT FUNCTION ==========")

def calculate_square(number):

    return number * number

user_number = int(input("Enter a number: "))

square_result = calculate_square(user_number)

print("Square of Number :", square_result)

print("\n========== PROGRAM COMPLETED ==========")
