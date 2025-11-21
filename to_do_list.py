# ------------------------------------------------------------
# 📝 PROJECT 3 : TO-DO LIST APPLICATION
# Developed by: [Sakthi]
# Description : A stylish interactive to-do list manager in Python
# ------------------------------------------------------------

import os
import time

# Task storage (in-memory)
tasks = []

# Clear screen for better UI
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Header display
def show_header():
    clear_screen()
    print("=" * 60)
    print("🗒️  PYTHON TO-DO LIST MANAGER  🧠".center(60))
    print("=" * 60)
    print()

# Display all tasks
def show_tasks():
    if not tasks:
        print("📭 No tasks found. Add a new one!\n")
        return

    print("🧾 Your Current Tasks:")
    print("-" * 60)
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        print(f"{i}. {task['title']}  [{status}]  - Priority: {task['priority']}")
    print("-" * 60)
    print()

# Add a new task
def add_task():
    title = input("🆕 Enter task title: ").strip()
    if not title:
        print("⚠️  Task cannot be empty!")
        time.sleep(1.5)
        return

    priority = input("🎯 Enter priority (High/Medium/Low): ").capitalize()
    if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"

    tasks.append({'title': title, 'done': False, 'priority': priority})
    print("✅ Task added successfully!")
    time.sleep(1.5)

# Mark a task as complete
def mark_complete():
    show_tasks()
    if not tasks:
        time.sleep(1.5)
        return
    try:
        task_no = int(input("✔️ Enter task number to mark complete: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]['done'] = True
            print("🎉 Task marked as complete!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")
    time.sleep(1.5)

# Edit a task
def edit_task():
    show_tasks()
    if not tasks:
        time.sleep(1.5)
        return
    try:
        task_no = int(input("✏️ Enter task number to edit: "))
        if 1 <= task_no <= len(tasks):
            new_title = input("🪶 Enter new task title: ").strip()
            if new_title:
                tasks[task_no - 1]['title'] = new_title
                print("📝 Task updated successfully!")
            else:
                print("⚠️ Task title cannot be empty.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")
    time.sleep(1.5)

# Delete a task
def delete_task():
    show_tasks()
    if not tasks:
        time.sleep(1.5)
        return
    try:
        task_no = int(input("🗑️ Enter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            deleted = tasks.pop(task_no - 1)
            print(f"🗑️ Task '{deleted['title']}' deleted successfully!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")
    time.sleep(1.5)

# Main loop
def todo_app():
    while True:
        show_header()
        show_tasks()

        print("Select an option:")
        print("1️⃣  Add Task")
        print("2️⃣  Mark Task as Complete")
        print("3️⃣  Edit Task")
        print("4️⃣  Delete Task")
        print("5️⃣  Exit")
        print("-" * 60)

        choice = input("👉 Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            mark_complete()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\n💡 Exiting To-Do List... Stay productive! ✨")
            break
        else:
            print("\n❌ Invalid choice! Try again.")
            time.sleep(1.5)

# Run program
if __name__ == "__main__":
    todo_app()
