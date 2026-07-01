"""Interactive terminal interface for the Python task manager showcase."""

from task_manager import TaskManager


def show_menu() -> None:
    """Display the available menu options."""
    print("\nTASK MANAGER CLI")
    print("=" * 24)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Search Task")
    print("5. Update Task")
    print("6. Save Tasks")
    print("7. Exit")
    print("=" * 24)


def get_task_number(manager: TaskManager) -> int:
    """Prompt the user for a valid task number."""
    manager.view_tasks()
    selection = input("Enter task number: ").strip()
    try:
        return int(selection)
    except ValueError as exc:
        raise ValueError("Please enter a valid number.") from exc


def main() -> None:
    """Run the interactive CLI loop so the user can manage tasks from the terminal."""
    manager = TaskManager()
    manager.load_tasks()

    while True:
        try:
            show_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                title = input("Task title: ").strip()
                description = input("Description: ").strip()
                priority = input("Priority (High/Medium/Low): ").strip() or "Medium"
                status = input("Status (Pending/Completed): ").strip() or "Pending"
                manager.add_task(title, description, priority, status)

            elif choice == "2":
                manager.view_tasks()

            elif choice == "3":
                if not manager.tasks:
                    print("No tasks available to delete.")
                    continue
                selection = get_task_number(manager)
                manager.delete_task(selection)

            elif choice == "4":
                keyword = input("Search keyword: ").strip()
                manager.search_task(keyword)

            elif choice == "5":
                if not manager.tasks:
                    print("No tasks available to update.")
                    continue
                selection = get_task_number(manager)
                new_title = input("New title (leave blank to keep current): ").strip()
                new_description = input("New description (leave blank to keep current): ").strip()
                new_priority = input("New priority (High/Medium/Low, leave blank to keep current): ").strip()
                new_status = input("New status (Pending/Completed, leave blank to keep current): ").strip()
                manager.update_task(
                    selection,
                    title=new_title or None,
                    description=new_description or None,
                    priority=new_priority or None,
                    status=new_status or None,
                )

            elif choice == "6":
                manager.save_tasks()

            elif choice == "7":
                manager.save_tasks()
                print("Goodbye!")
                break

            else:
                print("Please choose a valid option.")

        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            break
        except ValueError as exc:
            print(f"Input error: {exc}")


if __name__ == "__main__":
    main()
