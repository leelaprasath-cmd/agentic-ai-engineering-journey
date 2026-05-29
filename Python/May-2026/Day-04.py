# ==========================================
# DAY 04 — CONDITIONAL STATEMENTS
# ==========================================

print("========== STUDENT ELIGIBILITY SYSTEM ==========")

student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
student_mark = int(input("Enter your mark: "))

print("\nWelcome", student_name)


print("\n========== IF CONDITION ==========")

if student_mark >= 90:
    print("Excellent Performance!")


print("\n========== IF - ELSE CONDITION ==========")

if student_age >= 18:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")



print("\n========== IF - ELIF - ELSE CONDITION ==========")

if student_mark >= 90:
    print("Grade: A")
elif student_mark >= 75:
    print("Grade: B")
elif student_mark >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")


print("\n========== NESTED IF ==========")

attendance = int(input("Enter attendance percentage: "))

if attendance >= 75:
    if student_mark >= 50:
        print("Eligible for Exam")
    else:
        print("Not eligible due to low marks")
else:
    print("Not eligible due to low attendance")


print("\n========== PROGRAM COMPLETED ==========")
