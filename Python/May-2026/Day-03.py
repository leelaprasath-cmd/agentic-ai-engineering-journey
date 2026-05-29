# ==========================================
# DAY 03 — INPUT HANDLING & OPERATORS
# ==========================================

print("========== STUDENT INFORMATION ==========")

student_name = input("Enter your name: ")
college_name = input("Enter your college name: ")

print("\nWelcome", student_name)
print("College:", college_name)



print("\n========== ARITHMETIC OPERATORS ==========")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division       :", num1 / num2)
print("Modulus        :", num1 % num2)
print("Exponent       :", num1 ** num2)
print("Floor Division :", num1 // num2)



print("\n========== COMPARISON OPERATORS ==========")

print("num1 > num2  :", num1 > num2)
print("num1 < num2  :", num1 < num2)
print("num1 == num2 :", num1 == num2)
print("num1 != num2 :", num1 != num2)


print("\n========== LOGICAL OPERATORS ==========")

age = int(input("Enter your age: "))

print("Eligible for College and Adult:",
      age >= 18 and age <= 25)

print("Teenager or Adult:",
      age >= 13 or age >= 18)

print("Not Minor:",
      not(age < 18))



print("\n========== ASSIGNMENT OPERATORS ==========")

value = 10

print("Initial Value:", value)

value += 5
print("After += :", value)

value -= 3
print("After -= :", value)

value *= 2
print("After *= :", value)
