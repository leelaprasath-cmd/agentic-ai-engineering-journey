# Smart Study Session Tracker

python_time = 0
math_time = 0
science_time = 0
english_time = 0

daily_goal = 180  


def show_menu():
    print("\n===== SMART STUDY SESSION TRACKER =====")
    print("1. Add Study Session")
    print("2. View Study Summary")
    print("3. Check Daily Goal")
    print("4. Exit")


def add_study_session():
    global python_time, math_time, science_time, english_time

    print("\nAvailable subjects: Python, Math, Science, English")

    subject = input("Enter subject name: ").lower()
    minutes = int(input("Enter study time (minutes): "))

    if minutes <= 0:
        print("Please enter a valid study time.")
        return

    if subject == "python":
        python_time += minutes
        print(f"{minutes} minutes added to Python.")

    elif subject == "math":
        math_time += minutes
        print(f"{minutes} minutes added to Math.")

    elif subject == "science":
        science_time += minutes
        print(f"{minutes} minutes added to Science.")

    elif subject == "english":
        english_time += minutes
        print(f"{minutes} minutes added to English.")

    else:
        print("Invalid subject name.")


def show_summary():
    total_time = (
        python_time
        + math_time
        + science_time
        + english_time
    )

    print("\n===== STUDY SUMMARY =====")
    print(f"Python  : {python_time} mins")
    print(f"Math    : {math_time} mins")
    print(f"Science : {science_time} mins")
    print(f"English : {english_time} mins")
    print("-----------------------------")
    print(f"Total Study Time: {total_time} mins")


def check_goal():
    total_time = (
        python_time
        + math_time
        + science_time
        + english_time
    )

    print("\n===== DAILY GOAL STATUS =====")
    print(f"Goal: {daily_goal} mins")
    print(f"Completed: {total_time} mins")

    if total_time >= daily_goal:
        print("Congratulations! Daily study goal achieved.")
    else:
        remaining = daily_goal - total_time
        print(f"You need {remaining} more minutes to reach your goal.")


# Main program loop
running = True

while running:
    show_menu()

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_study_session()

    elif choice == "2":
        show_summary()

    elif choice == "3":
        check_goal()

    elif choice == "4":
        print("Exiting Smart Study Session Tracker...")
        running = False

    else:
        print("Invalid option. Please try again.")
