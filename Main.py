# Main

import Menu


# display program name and menu options
menu1 = Menu.Menu()
menu1.displayProgramName()
menu1.displayMenu()

print("\nPlease enter the number of your choice?")
choice = int(input())
while choice > 0 or choice < 6:

    print(choice)
    if choice == 1:
        menu1.add()
        choice = 0
    elif choice == 2:
        menu1.remove()
        choice = 0
    elif choice == 3:
        menu1.edit()
        choice = 0
    elif choice == 4:
        menu1.swap()
        choice = 0
    elif choice == 5:
        menu1.display()
        choice = 0
#print("That is not a valid integer. Please enter number between 1 and 5")
#choice = int(input())









