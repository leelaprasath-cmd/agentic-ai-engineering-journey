"""Task management logic for a Python concepts showcase."""

from datetime import datetime
from typing import Any, Dict, List, Optional

from decorators import log_action
from generators import task_generator
from storage import save_tasks


class TaskManager:
    """Manage tasks while demonstrating core Python concepts."""

    def __init__(self) -> None:
        self.tasks: List[Dict[str, Any]] = []

    def load_tasks(self) -> List[Dict[str, Any]]:
        """Load tasks from storage into memory."""
        from storage import load_tasks as storage_load_tasks

        try:
            self.tasks = storage_load_tasks()
        except Exception as exc:
            print(f"Unable to load tasks: {exc}")
            self.tasks = []
        else:
            return self.tasks
        finally:
            print("Task refresh complete.")

    @log_action("Task added successfully")
    def add_task(
        self,
        title: str,
        description: str = "",
        priority: str = "Medium",
        status: str = "Pending",
    ) -> Optional[Dict[str, Any]]:
        """Create and store a new task from provided values."""
        try:
            if not title.strip():
                raise ValueError("Title cannot be empty.")

            normalized_priority = priority.capitalize()
            if normalized_priority not in {"High", "Medium", "Low"}:
                raise ValueError("Priority must be High, Medium, or Low.")

            normalized_status = status.capitalize()
            if normalized_status not in {"Pending", "Completed"}:
                raise ValueError("Status must be Pending or Completed.")

            task = {
                "title": title.strip(),
                "description": description.strip(),
                "priority": normalized_priority,
                "status": normalized_status,
                "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            self.tasks.append(task)
            save_tasks(self.tasks)
            return task
        except ValueError as exc:
            print(f"Input error: {exc}")
            return None
        except Exception as exc:
            print(f"Unexpected error while adding task: {exc}")
            return None

    @log_action("Tasks displayed successfully")
    def view_tasks(self) -> List[Dict[str, Any]]:
        """Show all tasks using a generator."""
        try:
            if not self.tasks:
                print("No tasks available.")
                return []

            print("\nCurrent tasks:")
            for index, task in enumerate(task_generator(self.tasks), start=1):
                print(f"\n[{index}] {task['title']}")
                print(f"   Description: {task['description']}")
                print(f"   Priority: {task['priority']}")
                print(f"   Status: {task['status']}")
                print(f"   Created: {task['created_date']}")
            return self.tasks
        except KeyError as exc:
            print(f"Task data is incomplete: {exc}")
            return []
        except Exception as exc:
            print(f"Unexpected error while displaying tasks: {exc}")
            return []

    @log_action("Task updated successfully")
    def update_task(
        self,
        selection: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        priority: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """Update a selected task using optional values."""
        try:
            if not self.tasks:
                print("No tasks available to update.")
                return None

            index = selection - 1
            if index < 0 or index >= len(self.tasks):
                raise IndexError("Task number is out of range.")

            task = self.tasks[index]
            task["title"] = title.strip() if title is not None and title.strip() else task["title"]
            task["description"] = description.strip() if description is not None else task["description"]

            if priority is not None:
                task["priority"] = priority.capitalize()
                if task["priority"] not in {"High", "Medium", "Low"}:
                    raise ValueError("Priority must be High, Medium, or Low.")

            if status is not None:
                task["status"] = status.capitalize()
                if task["status"] not in {"Pending", "Completed"}:
                    raise ValueError("Status must be Pending or Completed.")

            save_tasks(self.tasks)
            return task
        except ValueError as exc:
            print(f"Input error: {exc}")
            return None
        except IndexError as exc:
            print(f"Selection error: {exc}")
            return None
        except Exception as exc:
            print(f"Unexpected error while updating task: {exc}")
            return None

    @log_action("Task deleted successfully")
    def delete_task(self, selection: int) -> Optional[Dict[str, Any]]:
        """Remove a selected task from the list."""
        try:
            if not self.tasks:
                print("No tasks available to delete.")
                return None

            index = selection - 1
            if index < 0 or index >= len(self.tasks):
                raise IndexError("Task number is out of range.")

            deleted_task = self.tasks.pop(index)
            save_tasks(self.tasks)
            return deleted_task
        except IndexError as exc:
            print(f"Selection error: {exc}")
            return None
        except Exception as exc:
            print(f"Unexpected error while deleting task: {exc}")
            return None

    @log_action("Search completed successfully")
    def search_task(self, keyword: str) -> List[Dict[str, Any]]:
        """Search tasks by title or description."""
        try:
            normalized_keyword = keyword.strip().lower()
            if not normalized_keyword:
                raise ValueError("Search keyword cannot be empty.")

            matches = [
                task for task in task_generator(self.tasks)
                if normalized_keyword in task["title"].lower() or normalized_keyword in task["description"].lower()
            ]

            if not matches:
                print("No matching tasks found.")
                return []

            print("\nMatching tasks:")
            for index, task in enumerate(matches, start=1):
                print(f"\n[{index}] {task['title']}")
                print(f"   Priority: {task['priority']}")
                print(f"   Status: {task['status']}")
            return matches
        except ValueError as exc:
            print(f"Input error: {exc}")
            return []
        except Exception as exc:
            print(f"Unexpected error while searching tasks: {exc}")
            return []

    def save_tasks(self) -> bool:
        """Persist the current task list to storage."""
        return save_tasks(self.tasks)
