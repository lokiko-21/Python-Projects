import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoList:
    def __init__(self):
        # initializes empty list to store tasks
        self.tasks = []

    # method for adding new tasks
    def add_task(self, task):
        self.tasks.append(task)
        display_tasks()

    # method for removing existing tasks
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

    # method for saving tasks to a text.txt file
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = [] # if files don't exist, it initializes tasks as an empty list

    # method for editing existing tasks
    def edit_task(self, event=None):
        selected_index = task_list.curselection()
        if selected_index:
            task = task_list.get(selected_index)
            new_task = simpledialog.askstring("Edit Task", "Enter the new task:", initialvalue=task)
            if new_task:
                self.tasks[selected_index[0]] = new_task
                display_tasks()
        else:
            messagebox.showinfo("Message", "Please select task to edit.")

def add_task(event=None):
    task = entry_task.get()
    if task:
        todo_list.add_task(task)
        entry_task.delete(0, tk.END)
        todo_list.save_tasks()

def remove_task(event=None):
    todo_list.remove_task()
    todo_list.save_tasks()

def display_tasks():
    todo_list.task_list.delete(0, tk.END)
    for task in todo_list.tasks:
        task_list.insert(tk.END, task)


# instance of ToDoList class
todo_list = ToDoList()

# main application window
window = tk.Tk()
window.title("To-Do List")

window.resizable(True, True)

# load tasks from file before displaying GUI components
todo_list.load_tasks()

# GUI components
label_task = tk.Label(window, text="Enter Task:")
label_task.grid(row=0, column=0)

entry_task = tk.Entry(window, width=30)
entry_task.grid(row=0, column=1)
entry_task.focus_set()

# display tasks immediately after loading GUI ocmponents
display_tasks()

# buttons for adding, removing, and editing tasks
button_add = tk.Button(window, text="Add Task", command=add_task)
button_add.grid(row=1, column=0)

button_remove = tk.Button(window, text="Remove Selected Task", command=remove_task)
button_remove.grid(row=1, column=1)

button_edit = tk.Button(window, text="Edit Task", command=todo_list.edit_task)
button_edit.grid(row=1, column=2)

# listbox to display tasks
task_list = tk.Listbox(window, width=40)
task_list.grid(row=2, columnspan=3)

# shortcuts
window.bind("<Control-d>", remove_task)
window.bind("<Control-Return>", add_task)
task_list.bind("<Double-1>", todo_list.edit_task)

# start tkinter event loop
window.mainloop()