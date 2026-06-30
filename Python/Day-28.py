# ==========================================
# DAY 28 — TASK MANAGER
# ==========================================

tasks = []


def show_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully.")


def view_tasks():

    if not tasks:
        print("No tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def remove_task():

    view_tasks()

    if not tasks:
        return

    task_number = int(input("\nEnter task number to remove: "))

    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"{removed} removed successfully.")
    else:
        print("Invalid task number.")


def main():

    while True:

        show_menu()

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Exiting Task Manager...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
