# Menu class


class Menu:

    def __init__(self):
        self.menuOptions = []
        self.menuOptions.append("1) Add item to list.")
        self.menuOptions.append("2) Remove item from list.")
        self.menuOptions.append("3) Edit item in list.")
        self.menuOptions.append("4) Swap 2 tasks.")
        self.menuOptions.append("5) Display the list.")
        self.menuOptions.append("6) Exit program.")
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
        taskToAdd = input("Please enter the NAME of the task you would like to add\n")
        self.toDoTasks.append(taskToAdd)
        return

    def remove(self):
        self.display()
        taskToRemove = int(input("Please enter the NUMBER of the task you would like to remove\n"))
        self.toDoTasks.pop(taskToRemove - 1)
        return

    def edit(self):
        self.display()
        taskToEdit = int(input("Choose the NUMBER of the item you want to edit.\n"))

        while 1:
            if taskToEdit < 1 or taskToEdit > len(self.toDoTasks):
                taskToEdit = int(input("Invalid option, please choose another\n"))
            else:
                break

        taskTextToEdit = input("Enter the desired task to replace the current one.\n")

        self.toDoTasks[taskToEdit - 1] = taskTextToEdit
        return

    def swap(self):
        task1 = int(input("Enter the NUMBER of the first item you want to swap\n"))
        while 1:
            if task1 < 1 or task1 > len(self.toDoTasks):
                task1 = int(input("Invalid option, please choose another\n"))
            else:
                break

        task2 = int(input("Enter the NUMBER of the second item you want to swap\n"))
        while 1:
            if task2 < 1 or task2 > len(self.toDoTasks):
                task2 = int(input("Invalid option, please choose another\n"))
            else:
                break

        temp = self.toDoTasks[task1 - 1]
        self.toDoTasks[task1 - 1] = self.toDoTasks[task2 - 1]
        self.toDoTasks[task2 - 1] = temp
        return

    def display(self):
        print(self.toDoTasks)
        return

