
# To-Do List CLI Application

A command-line interface (CLI) application for managing a to-do list. This application allows users to add, view, remove, and change the status of tasks. The tasks are saved in a JSON file for persistence.

## Features

- Add new tasks with a name and description
- View all tasks with their details
- Remove a task by its index
- Change the status of a task (completed/pending)
- Persistent storage of tasks using a JSON file

## Requirements

- Python 3.x
- `termcolor` library for colored text in the terminal
- `pyfiglet` library for ASCII art text
- `inquirer` library for interactive menu prompts

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todo-list-cli.git
    cd todo-list-cli
    ```

2. Install the required libraries:
    ```bash
    pip install termcolor pyfiglet inquirer
    ```

## Usage

Run the application:
```bash
python your_script_name.py
```

You will be presented with a menu to manage your to-do list:

```
To-Do List Menu
1. Add Task
2. View Tasks
3. Remove Task
4. Change Task Status
5. Exit
```

### Adding a Task

Select "Add Task" and follow the prompts to enter the task name and description.

### Viewing Tasks

Select "View Tasks" to see a list of all tasks with their details.

### Removing a Task

Select "Remove Task" and enter the task index to remove it from the list.

### Changing Task Status

Select "Change Task Status" and enter the task index and new status (true for completed, false for pending).

### Exiting

Select "Exit" to exit the program.

## Example

```bash
python your_script_name.py
```

```
To-Do List Menu
1. Add Task
2. View Tasks
3. Remove Task
4. Change Task Status
5. Exit
Enter your choice: 2

Task 1:
--------------------
Project: Grocery Shopping
Description: Buy groceries for the week
Start date: 2024-07-15
Status: Completed
--------------------

Task 2:
--------------------
Project: Project Meeting
Description: Attend the project kickoff meeting
Start date: 2024-07-16
Status: Pending
--------------------
```
