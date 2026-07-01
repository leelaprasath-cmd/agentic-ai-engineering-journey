"""Decorators for the Task Manager CLI application."""

from functools import wraps


def log_action(success_message="Operation completed successfully"):
    """Log method entry, success, and completion using a decorator."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("-" * 36)
            print(f"Running {func.__name__}()")
            print("-" * 36)
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                print(f"Error during {func.__name__}: {exc}")
                return None
            else:
                print(success_message)
                return result
            finally:
                print("-" * 36)
                print(f"Finished {func.__name__}()")
                print("-" * 36)

        return wrapper

    return decorator
