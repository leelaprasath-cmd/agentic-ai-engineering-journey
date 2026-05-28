# Single Program Using if-elif-else

import random
import math

print("1. Number Guessing Game")
print("2. Interest Calculator")
print("3. Multiplication Table")
print("4. Word Counter")
print("5. FizzBuzz With Twist")

choice = input("\nEnter your choice (1-5): ")



if choice == "1":

    print("\n===== NUMBER GUESSING GAME =====")

    random_number = random.randint(1, 100)

    while True:

        guess = int(input("Guess a number between 1 and 100: "))

        if guess > random_number:
            print("Too High!")

        elif guess < random_number:
            print("Too Low!")

        else:
            print("Congratulations! You guessed correctly.")
            break




elif choice == "2":

    print("\n===== SIMPLE & COMPOUND INTEREST =====")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate: "))
    time = float(input("Enter time in years: "))

    # Simple Interest
    simple_interest = (principal * rate * time) / 100

    # Compound Interest
    compound_interest = principal * (
        math.pow((1 + rate / 100), time)
    ) - principal

    print(f"Simple Interest   : {simple_interest:.2f}")
    print(f"Compound Interest : {compound_interest:.2f}")




elif choice == "3":

    print("\n===== MULTIPLICATION TABLE =====")

    number = int(input("Enter a number: "))

    for i in range(1, 21):

        print(f"{number} x {i} = {number * i}")





elif choice == "4":

    print("\n===== WORD COUNTER =====")

    sentence = input("Enter a sentence: ")

    words = sentence.split()

    print(f"Total Words: {len(words)}")

    print("\nLetter Frequency:")

    checked_letters = ""

    for letter in sentence.lower():

        if letter.isalpha() and letter not in checked_letters:

            count = sentence.lower().count(letter)

            print(f"{letter} : {count}")

            checked_letters += letter




elif choice == "5":

    print("\n===== FIZZBUZZ WITH TWIST =====")

    for number in range(1, 101):

        if number % 15 == 0:
            print("FizzBuzz")

        elif number % 7 == 0:
            print("Boom")

        elif number % 5 == 0:
            print("Buzz")

        elif number % 3 == 0:
            print("Fizz")

        else:
            print(number)





else:

    print("\nInvalid Choice. Please run the program again.")

