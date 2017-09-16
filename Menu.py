# Menu class


class Menu:

    def __init__(self):
        self.menuOptions = []
        self.menuOptions.append("1) Add item to list.")
        self.menuOptions.append("2) Remove item from list.")
        self.menuOptions.append("3) Edit item in list.")
        self.menuOptions.append("4) Swap 2 tasks.")
        self.menuOptions.append("5) Display the list.")
        self.toDoTasks = []
        return

    def displayProgramName(self):
        print("Welcome to your To-Do List")
        return

    def displayMenu(self):
        for option in range(len(self.menuOptions)):
            print(self.menuOptions[option])
        return

    def add(self):
        print("Please enter the name of the task you would like to add")
        task = input()
        self.toDoTasks.append(task)
        print(self.toDoTasks)
        return

    def remove(self):
        return

    def edit(self):
        return

    def swap(self):
        return

    def display(self):
        return

