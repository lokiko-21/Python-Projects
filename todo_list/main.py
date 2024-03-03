import tkinter as tk

class ToDoList:
    def __init__(self):
        # initializes empty list to store tasks
        self.tasks = []

    # method to add task to To-Do List
    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the to-do list.')

    # method to remove tak from To-Do List
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed from the to-do list.')
        else:
            print(f'Task "{task}" not found in the to-do list.')

    # method to display tasks in the To-Do List
    def show_tasks(self):
        if self.tasks:
            print("To-Do List")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("To-Do List is empty.")


def add_task():
    task = entry_task.get()
    if task:
        todo_list.add_task(task)
        entry_task.delete(0, tk.END)
        display_tasks()

def remove_task():
    task = entry_task.get()
    if task:
        todo_list.remove_task(task)
        entry_task.delete(0, tk.END)
        display_tasks()

def display_tasks():
    task_list.delete(0, tk.END)
    for idx, task in enumerate(todo_list.tasks, start=1):
        task_list.insert(tk.END, f"{idx}. {task}")


todo_list = ToDoList()

window = tk.Tk()
window.title("To-Do List")

label_task = tk.Label(window, text="Enter Task:")
label_task.grid(row=0, column=0)

entry_task = tk.Entry(window, width=30)
entry_task.grid(row=0, column=1)

button_add = tk.Button(window, text="Add Task", command=add_task)
button_add.grid(row=1, column=0)

button_remove = tk.Button(window, text="Remove task", command=remove_task)
button_remove.grid(row=1, column=1)

task_list = tk.Listbox(window, width=40)
task_list.grid(row=2, columnspan=2)

display_tasks()

window.mainloop()