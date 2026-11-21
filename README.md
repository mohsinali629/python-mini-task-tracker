# Python Mini Task Tracker

A simple, menu-driven command-line Task Tracker built with Python 3. It allows users to manage daily tasks and automatically saves changes to a local JSON file (`tasks.json`) so tasks persist across sessions.

## Project Goal

Build an interactive Python application that demonstrates core programming concepts—lists, dictionaries, functions, loops, conditionals, exception handling, and JSON file persistence (`json.load` and `json.dump`).

## Features

- **Add Tasks:** Add new tasks with non-empty titles (stored as `Pending` by default).
- **View Tasks:** Display a numbered list of all tasks showing whether each is `[Pending]` or `[Done]`.
- **Complete Tasks:** Mark an existing task as completed (`Done`) by selecting its task number.
- **Delete Tasks:** Remove unwanted tasks by selecting their task number.
- **Automatic JSON Persistence:** Automatically saves updates to `tasks.json` after every change and reloads saved tasks on startup.
- **Robust Error Handling:** Gracefully handles missing/empty `tasks.json` files, blank task titles, non-numeric inputs, and out-of-range task or menu numbers.

## Project Files

- `mini_task_tracker.py` — Main Python source file containing the task tracker logic and CLI menu.
- `README.md` — Project documentation and usage instructions.
- `tasks.json` — Auto-generated JSON file storing task records (created upon adding the first task).

## How to Run

### Option 1: Run Locally (Terminal / Command Prompt)

1. Ensure Python 3 is installed on your machine.
2. Open a terminal in the project directory and run:
   ```bash
   python mini_task_tracker.py
   ```

### Option 2: Run in Google Colab

1. Open a new notebook in [Google Colab](https://colab.research.google.com/).
2. Upload `mini_task_tracker.py` to the Colab session files panel (or write it using `%%writefile mini_task_tracker.py`).
3. Run the script in a code cell:
   ```python
   !python mini_task_tracker.py
   ```
4. To verify persistence, exit the program (`5`) and re-run `!python mini_task_tracker.py` within the same Colab runtime—your previously saved tasks from `tasks.json` will reload automatically.

## Example Interaction

```text
TASK TRACKER
1. Add 2. View 3. Complete 4. Delete 5. Exit
Choice: 1
Task title: Read notes
Task added.

TASK TRACKER
1. Add 2. View 3. Complete 4. Delete 5. Exit
Choice: 2
1. Read notes [Pending]

TASK TRACKER
1. Add 2. View 3. Complete 4. Delete 5. Exit
Choice: 3
Task number: 1
Task completed.

TASK TRACKER
1. Add 2. View 3. Complete 4. Delete 5. Exit
Choice: 2
1. Read notes [Done]
```

# GitHub
[Open GitHUb](https://github.com/mohsinali629/python-mini-task-tracker)
