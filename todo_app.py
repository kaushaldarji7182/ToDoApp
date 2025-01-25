import tkinter as tk
from tkinter import messagebox
import os

# Global list to store tasks
tasks = []

TASKS_FILE = "tasks.txt"

def add_task():
    task = task_input.get().strip()  # Get the text from the input field
    if task != "":
        tasks.append({"task": task, "completed": False})  # Add task as a dictionary with completion status
        update_task_listbox()  # Update the listbox with the new task
        task_input.delete(0, tk.END)  # Clear the input field
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    try:
        selected_index = task_listbox.curselection()[0]  # Get the selected task index
        tasks.pop(selected_index)  # Remove the task from the list
        update_task_listbox()  # Update the listbox
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def mark_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

def clear_all_tasks():
    if tasks:
        confirm = messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?")
        if confirm:
            tasks.clear()  # Clear the task list
            update_task_listbox()  # Update the listbox
    else:
        messagebox.showwarning("No Tasks", "There are no tasks to clear.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)  # Clear the current list in the listbox
    for task in tasks:
        display_text = task["task"]
        if task["completed"]:
            display_text = f"✔ {display_text}"  # Add a checkmark for completed tasks
        task_listbox.insert(tk.END, display_text)  # Insert each task into the listbox

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            completed = "1" if task["completed"] else "0"
            f.write(f"{task['task']}|{completed}\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                task_text, completed = line.strip().split("|")
                tasks.append({"task": task_text, "completed": completed == "1"})
        update_task_listbox()

def exit_app():
    save_tasks()  # Save tasks before exiting
    root.quit()  # Close the app

# Create the main window
root = tk.Tk()
root.title("To-Do App")

# Create a frame for the listbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a listbox to display tasks
task_listbox = tk.Listbox(frame, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.pack(side=tk.LEFT)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)

# Create an entry widget for adding tasks
task_input = tk.Entry(root, width=50)
task_input.pack(pady=10)

# Create buttons for adding, removing tasks, and exiting
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", width=20, command=remove_task)
remove_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark Completed", width=20, command=mark_completed)
mark_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=20, command=clear_all_tasks)
clear_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", width=20, command=exit_app)
exit_button.pack(pady=5)

# Create a label to display a "Thank you for using" message at the bottom
thank_you_label = tk.Label(root, text="Thank you for using!", font=("Arial", 10))
thank_you_label.pack(pady=10)

# Load tasks from the file on startup
load_tasks()

# Start the main loop
root.mainloop()
