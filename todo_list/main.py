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
            print("\n===To-Do List===")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("\nTo-Do List is empty.")
    

# main function to run the To-Do List application
def main():
    todo_list = ToDoList()

    while True:
        # display menu
        print("\n1 - Add Task")
        print("2 - Remove Task")
        print("3 - Show Tasks")
        print("4 - Exit")

        #get user input
        choice = input("\nEnter your choice: ")

        # inpu handler
        if choice == '1':
            task = input("\nEnter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("\nEnter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("\nexisting program.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    # run main function when script is executed
    main()