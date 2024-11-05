
# To do list Application 

import datetime

tasks = [ ]

def add_task():

    title = input ("Enter the task title: ")
    priority = input("Enter the task priority (High, Medium, Low): ")
    due_date = input("Enter the due date (MM-DD-YYYY): ")

    try:
        due_date = datetime.datetime.strptime(due_date, " MM-DD-YYYY").date()
    except ValueError:
        print("Invalide date format. Task added without a due date.")
        due_date = None
     
    tasks.append({"title": title, "status": "Incomplete", "priority": priority, "due_date": due_date})
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for index, task in enumerate (tasks, start=1):
            if task['status'] == 'Complete':
                color = "\033[92m"                 # Green for Complete
            else:
                color = "\033[91m"                 # Red for Incomplete
            reset_color = "\033[0m"
            print(f"{index}. {task['title']} -{task['status']}")

def mark_task_complete():
    try:
        view_tasks()
        task_number = int(input("Enter the task number to mark as complete:"))
        if 1<= task_number <= len(tasks):
            tasks[task_number -1]["status"] = "complete"
            print ("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    try:
        view_tasks()
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number -1)
            print(f"Task '{removed_task['title']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    # The main function to rub To Do list Application 
    while True:
        print("\nWelcome to the To-Do list App!")
        print("Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark  task as complete")
        print("4. Delete a task")
        print("5. Quit")

        try:
            choice = int(input("Choose an option (1-5): "))

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Goodbye!")
                break 
            else:
                print("Invalid chioce. Please choose a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")

        finally:
            print("Thank you for using the To Do list App.")

main()