# ==========================================
# DAY 11 — EXCEPTION HANDLING PRACTICE
# ==========================================

print("===== SIMPLE CALCULATOR =====")

try:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("\n===== RESULTS =====")

    print("Addition       :", num1 + num2)
    print("Subtraction    :", num1 - num2)
    print("Multiplication :", num1 * num2)
    print("Division       :", num1 / num2)

except ValueError:

    print("Error: Please enter valid numbers.")

except ZeroDivisionError:

    print("Error: Division by zero is not allowed.")

except Exception as error:

    print("Unexpected Error:", error)

finally:

    print("\nProgram Finished.")

