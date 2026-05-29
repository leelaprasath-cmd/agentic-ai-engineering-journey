# ==========================================
# DAY 09 — DICTIONARY PRACTICE
# ==========================================

print("===== STUDENT PROFILE SYSTEM =====")


student = {}

student["name"] = input("Enter your name: ")
student["department"] = input("Enter your department: ")
student["college"] = input("Enter your college name: ")
student["age"] = int(input("Enter your age: "))


print("\n===== STUDENT DETAILS =====")

print("Name       :", student["name"].title())
print("Department :", student["department"].upper())
print("College    :", student["college"].title())
print("Age        :", student["age"])


print("\n===== DICTIONARY METHODS =====")

print("Keys   :", student.keys())
print("Values :", student.values())
print("Items  :", student.items())


search_key = input("\nEnter key to search: ").lower()

if search_key in student:

    print("Key Found")
    print("Value :", student[search_key])

else:

    print("Key Not Found")


student["goal"] = "AI Engineer"

print("\nUpdated Dictionary:")
print(student)



print("\n===== PROGRAM COMPLETED =====")
