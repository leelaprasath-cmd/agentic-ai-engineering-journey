# ==========================================
# DAY 23 — ERROR HANDLING
# ==========================================

print("===== STUDENT MARKS CALCULATOR =====")

while True:

    try:
        name = input("\nEnter Student Name: ")

        marks1 = int(input("Enter Python Marks: "))
        marks2 = int(input("Enter AI Marks: "))
        marks3 = int(input("Enter Math Marks: "))

        total = marks1 + marks2 + marks3
        average = total / 3

    except ValueError:
        print("\nInvalid input! Please enter only numbers for marks.")

    except ZeroDivisionError:
        print("\nCannot divide by zero.")

    else:
        print("\n===== RESULT =====")
        print(f"Student : {name}")
        print(f"Total   : {total}")
        print(f"Average : {average:.2f}")

        if average >= 90:
            print("Grade   : A")

        elif average >= 75:
            print("Grade   : B")

        elif average >= 50:
            print("Grade   : C")

        else:
            print("Grade   : Fail")

    finally:
        print("\nProgram execution completed.")

    choice = input("\nDo you want to calculate another result? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using the Student Marks Calculator!")
        break
