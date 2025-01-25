import tkinter as tk
from tkinter import messagebox

# Global list to store tasks
tasks = []

def add_task():
    task = task_input.get().strip()  # Get the text from the input field
    if task != "":
        tasks.append(task)
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

def update_task_listbox():
    task_listbox.delete(0, tk.END)  # Clear the current list in the listbox
    for task in tasks:
        task_listbox.insert(tk.END, task)  # Insert each task into the listbox

def exit_app():
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

exit_button = tk.Button(root, text="Exit", width=20, command=exit_app)
exit_button.pack(pady=5)

# Start the main loop
root.mainloop()
