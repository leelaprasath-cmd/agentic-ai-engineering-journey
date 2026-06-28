# ==========================================
# DAY 24 — CUSTOM EXCEPTIONS, raise & assert
# ==========================================


class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass


while True:

    try:
        name = input("\nEnter your name: ")
        age = int(input("Enter your age: "))

        assert age > 0, "Age must be greater than 0."

        if age < 18:
            raise InvalidAgeError("You must be at least 18 years old.")

    except ValueError:
        print("Please enter a valid number.")

    except AssertionError as error:
        print(error)

    except InvalidAgeError as error:
        print(error)

    else:
        print("\n===== REGISTRATION SUCCESSFUL =====")
        print(f"Name : {name}")
        print(f"Age  : {age}")

    finally:
        print("Registration process completed.")

    choice = input("\nRegister another user? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you!")
        break
