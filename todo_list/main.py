import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        # initializes empty list to store tasks
        self.tasks = []

    # method to add task to To-Do List
    def add_task(self, task):
        self.tasks.append(task)
        display_tasks()

    # method to remove tak from To-Do List
    def remove_task(self):
        selected_index = task_list.curselection()
        if selected_index:
            task = task_list.get(selected_index)
            confirm = messagebox.askyesno("Confirm", f"Are you done with the task '{task}'?")
            if confirm:
                self.tasks.remove(task)
                display_tasks()
        else:
            messagebox.showinfo("Message", "Please select task to remove.")


def add_task():
    task = entry_task.get()
    if task:
        todo_list.add_task(task)
        entry_task.delete(0, tk.END)

def remove_task():
    todo_list.remove_task()

def display_tasks():
    task_list.delete(0, tk.END)
    for task in todo_list.tasks:
        task_list.insert(tk.END, task)


# instance of ToDoList class
todo_list = ToDoList()

# main application window
window = tk.Tk()
window.title("To-Do List")

# GUI components
label_task = tk.Label(window, text="Enter Task:")
label_task.grid(row=0, column=0)

entry_task = tk.Entry(window, width=30)
entry_task.grid(row=0, column=1)

# buttons for adding and removing tasks
button_add = tk.Button(window, text="Add Task", command=add_task)
button_add.grid(row=1, column=0)

button_remove = tk.Button(window, text="Remove Selected Task", command=remove_task)
button_remove.grid(row=1, column=1)

# listbox to display tasks
task_list = tk.Listbox(window, width=40)
task_list.grid(row=2, columnspan=2)

# start tkinter event loop
window.mainloop()