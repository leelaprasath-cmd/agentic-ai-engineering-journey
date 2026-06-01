# ==========================================
# DAY 14 — PYTHON MINI PROJECT HUB
# ==========================================

import json

students = {}
contacts = []
cart = {}


while True:

    print("\n=================================")
    print("      PYTHON MINI PROJECT HUB")
    print("=================================")
    print("1. Student Gradebook")
    print("2. Word Frequency Counter")
    print("3. Shopping Cart")
    print("4. Contact Book")
    print("5. CSV Analyzer")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # ==========================================
    # STUDENT GRADEBOOK
    # ==========================================

    if choice == "1":

        print("\n===== STUDENT GRADEBOOK =====")

        n = int(input("How many students? "))

        total = 0

        for i in range(n):

            name = input("Student Name: ")
            marks = int(input("Marks: "))

            students[name] = marks
            total += marks

        average = total / len(students)

        print("\nClass Average:", average)

        print("\n===== RANK LIST =====")

        rank_list = sorted(
            students.items(),
            key=lambda x: x[1],
            reverse=True
        )

        rank = 1

        for student, marks in rank_list:

            print(rank, "-", student, "-", marks)

            rank += 1

    # ==========================================
    # WORD FREQUENCY COUNTER
    # ==========================================

    elif choice == "2":

        print("\n===== WORD FREQUENCY COUNTER =====")

        paragraph = input("Enter a paragraph:\n")

        words = paragraph.lower().split()

        frequency = {}

        for word in words:

            frequency[word] = frequency.get(word, 0) + 1

        print("\nTop Words:")

        sorted_words = sorted(
            frequency.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for word, count in sorted_words[:10]:

            print(word, ":", count)

    # ==========================================
    # SHOPPING CART
    # ==========================================

    elif choice == "3":

        print("\n===== SHOPPING CART =====")

        while True:

            print("\n1. Add Item")
            print("2. Remove Item")
            print("3. View Total")
            print("4. Save Cart")
            print("5. Back")

            cart_choice = input("Choose: ")

            if cart_choice == "1":

                item = input("Item Name: ")
                price = float(input("Price: "))

                cart[item] = price

            elif cart_choice == "2":

                item = input("Item to Remove: ")

                if item in cart:
                    del cart[item]

            elif cart_choice == "3":

                total = sum(cart.values())

                print("Total Price:", total)

            elif cart_choice == "4":

                with open("cart.json", "w") as file:

                    json.dump(cart, file, indent=4)

                print("Cart Saved.")

            elif cart_choice == "5":

                break

    # ==========================================
    # CONTACT BOOK
    # ==========================================

    elif choice == "4":

        print("\n===== CONTACT BOOK =====")

        while True:

            print("\n1. Add Contact")
            print("2. Search Contact")
            print("3. Delete Contact")
            print("4. Back")

            contact_choice = input("Choose: ")

            if contact_choice == "1":

                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")

                contacts.append(
                    {
                        "name": name,
                        "phone": phone,
                        "email": email
                    }
                )

            elif contact_choice == "2":

                search = input("Search Name: ")

                for contact in contacts:

                    if contact["name"].lower() == search.lower():

                        print(contact)

            elif contact_choice == "3":

                delete_name = input("Delete Name: ")

                contacts = [
                    c for c in contacts
                    if c["name"].lower() != delete_name.lower()
                ]

            elif contact_choice == "4":

                break

    # ==========================================
    # CSV ANALYZER
    # ==========================================

    elif choice == "5":

        print("\n===== CSV ANALYZER =====")

        filename = input("Enter CSV filename: ")

        try:

            with open(filename, "r") as file:

                rows = file.readlines()

            total = 0
            count = 0

            for row in rows[1:]:

                values = row.strip().split(",")

                for value in values:

                    try:
                        total += float(value)
                        count += 1
                    except:
                        pass

            if count > 0:

                print("Sum:", total)
                print("Average:", total / count)

        except FileNotFoundError:

            print("File not found.")

    # ==========================================
    # EXIT
    # ==========================================

    elif choice == "6":

        print("\nProgram Closed.")
        break

    else:

        print("\nInvalid Choice.")
