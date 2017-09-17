# Main

import Menu


# display program name and menu options
menu1 = Menu.Menu()
menu1.displayProgramName()
menu1.displayMenu()

print("\nPlease enter the number of your choice?")
choice = int(input())
exitPgm = 0

while exitPgm == 0:

    if choice == 1:
        menu1.add()
    elif choice == 2:
        menu1.remove()
    elif choice == 3:
        menu1.edit()
    elif choice == 4:
        menu1.swap()
    elif choice == 5:
        menu1.display()
    elif choice == 6:
        print("Program exiting")
        exitPgm = 1
        break
    else:
        print("Invalid option, please choose another")

    print("What would you like to do?")
    menu1.displayMenu()
    choice = int(input())










