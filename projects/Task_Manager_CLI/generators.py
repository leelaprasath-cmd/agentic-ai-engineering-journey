"""Generator helpers for the Task Manager CLI application."""

from typing import Iterable, Iterator, Dict, Any


def task_generator(tasks: Iterable[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:
    """Yield each task from a collection of tasks."""
    for task in tasks:
        yield task
