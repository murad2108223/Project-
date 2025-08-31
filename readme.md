# To-Do List Application

This is a simple command-line To-Do List application built in Python. The application allows users to add, remove, and list tasks, with persistent storage in a text file.

## Features
- **Persistent Storage**: The tasks are saved to a file (`todo_list.txt`), so you can pick up where you left off each time you run the program.
- **Add Tasks**: Allows you to add new tasks to your to-do list.
- **Remove Tasks**: You can remove tasks by specifying their number.
- **View Tasks**: Displays all tasks with corresponding numbers to make it easy to manage them.
- **Simple Command-Line Interface**: The program runs in the terminal or command prompt, providing a straightforward user experience.

---

## Installation

1. **Clone the repository** (or download the code file).

```bash
# If you want to clone it from GitHub (use your own repo link)ist.git
```

2. **Navigate to the project folder**.

```bash
cd todo-list
```

3. **Ensure Python 3.x is installed**.

```bash
python --version  # Should show Python 3.x.x
```

---

## Usage

### Running the Program

1. Open a terminal/command prompt.
2. Navigate to the directory where the `todo_list.py` script is located.
3. Run the script by typing:

```bash
python todo_list.py
```

### Commands in the Program

The program will display a menu with the following options:
1. **Add a Task**: Allows you to input a new task to the to-do list.
2. **Remove a Task**: You can select a task by its number and remove it.
3. **List Tasks**: Displays all tasks currently in your list with their task number.
4. **Quit**: Exits the program.

---

## How It Works

### Task Storage

Tasks are stored in a text file called `todo_list.txt`. If the file doesn’t exist, it will be created when the program is first run.

### Code Overview

- **`load_tasks()`**: Loads tasks from `todo_list.txt` into a Python list when the program starts.
- **`save_tasks(tasks)`**: Saves the tasks list to the `todo_list.txt` file.
- **`add_task(tasks)`**: Adds a new task to the list.
- **`remove_task(tasks)`**: Removes a task by its index (task number).
- **`list_tasks(tasks)`**: Displays the current list of tasks.
- **`main()`**: The main function running the command-line menu system.

---

## Customization

You can modify the following aspects of the project:

- **File Name**: Change the name of the task storage file (`todo_list.txt`).
- **Task Input Format**: You can modify how tasks are input or what kind of data you want to store with each task.
- **Additional Features**: You could add more features, such as:
  - Prioritizing tasks (low, medium, high priority).
  - Task due dates.
  - Ability to mark tasks as completed.

---

## Troubleshooting

1. **The `todo_list.txt` file is not being created.**
  - Ensure that the directory is writable and that the Python script has permission to create files.

2. **Getting an error when trying to add/remove tasks.**
  - Double-check your input to ensure you’re entering a valid task number when removing tasks.
  - Make sure the tasks file is not open in another program while the script is running.

---

## License

This project is open-source and available under the MIT License. See the LICENSE file for more information.
