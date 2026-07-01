"""JSON storage helpers for the Task Manager CLI application."""

import json
from pathlib import Path
from typing import Any, Dict, List

DATA_FILE = Path(__file__).resolve().parent / "tasks.json"


def load_tasks() -> List[Dict[str, Any]]:
    """Load tasks from the JSON file and create it when missing."""
    try:
        if not DATA_FILE.exists():
            raise FileNotFoundError("Task storage file does not exist yet.")

        with DATA_FILE.open("r", encoding="utf-8") as handle:
            tasks = json.load(handle)

        if not isinstance(tasks, list):
            raise ValueError("Stored task data must be a list.")

    except FileNotFoundError as exc:
        print(f"Storage note: {exc}")
        DATA_FILE.write_text("[]\n", encoding="utf-8")
        return []
    except json.JSONDecodeError as exc:
        print(f"Storage warning: invalid JSON ({exc}). Starting with an empty task list.")
        return []
    except ValueError as exc:
        print(f"Storage warning: {exc}")
        return []
    else:
        print(f"Loaded {len(tasks)} task(s) from storage.")
        return tasks
    finally:
        print("Storage check complete.")


def save_tasks(tasks: List[Dict[str, Any]]) -> bool:
    """Write the current task list to tasks.json."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as handle:
            json.dump(tasks, handle, indent=2)
            handle.write("\n")

    except (FileNotFoundError, OSError, TypeError, ValueError) as exc:
        print(f"Storage warning: unable to save tasks ({exc}).")
        return False
    else:
        print(f"Saved {len(tasks)} task(s) to storage.")
        return True
    finally:
        print("Storage save attempt complete.")
