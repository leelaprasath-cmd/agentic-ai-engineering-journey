# ==========================================
# DAY 27 — MODULES & __main__
# ==========================================

from math import sqrt
import math


def show_menu():
    print("\n===== SIMPLE MATH TOOL =====")
    print("1. Square Root")
    print("2. Power")
    print("3. Factorial")
    print("4. Exit")


def calculate_square_root():
    number = float(input("Enter a number: "))
    print(f"Square Root: {sqrt(number)}")


def calculate_power():
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    print(f"Result: {math.pow(base, exponent)}")


def calculate_factorial():
    number = int(input("Enter a positive integer: "))
    print(f"Factorial: {math.factorial(number)}")


def main():

    while True:

        show_menu()

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            calculate_square_root()

        elif choice == "2":
            calculate_power()

        elif choice == "3":
            calculate_factorial()

        elif choice == "4":
            print("\nExiting Program...")
            break

        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()
