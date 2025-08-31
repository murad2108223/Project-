import os

# File path to store tasks
FILE_PATH = 'todo_list.txt'

def load_tasks():
    """Load tasks from file."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(FILE_PATH, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    """Remove a task."""
    list_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def list_tasks(tasks):
    """Display the tasks."""
    if tasks:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks to show.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. List Tasks")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            list_tasks(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1-4.")

if __name__ == "__main__":
    main()
