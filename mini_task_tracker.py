import json

TASKS_FILE = "tasks.json"

# Im also declearing types for clear clibased task tracker
def load_tasks(filename: str = TASKS_FILE) -> list[dict]:
    """Load tasks from a JSON file, returning an empty list if missing or invalid."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks: list[dict], filename: str = TASKS_FILE) -> None:
    """Save the current list of tasks to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks: list[dict]) -> None:
    """Prompt for a task title, validate it, append as Pending, and save."""
    title = input("Task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks: list[dict]) -> None:
    """Display all tasks with their 1-based index and Pending/Done status."""
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task.get("done") else "Pending"
        print(f"{index}. {task.get('title', '')} [{status}]")


def complete_task(tasks: list[dict]) -> None:
    """Prompt for a task number, mark it as Done, and save."""
    if not tasks:
        print("No tasks available to complete.")
        return

    try:
        task_number = int(input("Task number: "))
    except ValueError:
        print("Error: Please enter a valid numeric task number.")
        return

    if task_number < 1 or task_number > len(tasks):
        print(f"Error: Task number must be between 1 and {len(tasks)}.")
        return

    tasks[task_number - 1]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks: list[dict]) -> None:
    """Prompt for a task number, remove the task from the list, and save."""
    if not tasks:
        print("No tasks available to delete.")
        return

    try:
        task_number = int(input("Task number: "))
    except ValueError:
        print("Error: Please enter a valid numeric task number.")
        return

    if task_number < 1 or task_number > len(tasks):
        print(f"Error: Task number must be between 1 and {len(tasks)}.")
        return

    tasks.pop(task_number - 1)
    save_tasks(tasks)
    print("Task deleted.")


def main() -> None:
    """Run the main interactive menu loop for the Task Tracker."""
    tasks = load_tasks()

    while True:
        print("\nTASK TRACKER")
        print("1. Add 2. View 3. Complete 4. Delete 5. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()
