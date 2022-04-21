# Author: Gan Li
# Project: Personal Library Management System
# Version: 0.1 Minimum Viable Product
# Course: CS 361
# File Description: This is the main file of this project
"""
Project Design:
    Library: list of books saved in xlsx
    User Interface
    Users: list of users saved in xlsx
"""
import Book
import UI


if __name__ == '__main__':
    UI.clear()  # clear screen
    UI.homePage()
    choice = input("PLEASE TYPE IN ONE OF THE ABOVE INDICES (1 - 6): ")
    while True:
        # choice 1: view the library
        if choice == '1':
            UI.clear()
            UI.category()
            Book.listByCategory()
            catAnswer = input("Enter Y to view another category.\nEnter N to Home Page.\n")
            while catAnswer != 'Y' and catAnswer != 'N':
                catAnswer = input("\nINVALID INPUT\nPLEASE TYPE Y/N: ")
            if catAnswer == 'Y':
                continue
            else:
                UI.clear()  # clear screen
                UI.homePage()
                choice = input("PLEASE TYPE IN ONE OF THE ABOVE INDICES (1 - 6): ")
        # choice 2: add a book
        elif choice == '2':
            UI.clear()
            Book.add()
            print("\nDo you want to add another book?")
            addAnswer = input("Enter Y to add another book.\nEnter N to Home Page.\n")
            while addAnswer != 'Y' and addAnswer != 'N':
                addAnswer = input("\nINVALID INPUT\nPLEASE TYPE Y/N: ")
            if addAnswer == 'Y':
                continue
            else:
                UI.clear()  # clear screen
                UI.homePage()
                choice = input("PLEASE TYPE IN ONE OF THE ABOVE INDICES (1 - 6): ")
        # choice 3: borrow a book
        elif choice == '3':
            UI.clear()
            Book.borrow()
            UI.clear()  # clear screen
            UI.homePage()
            choice = input("PLEASE TYPE IN ONE OF THE ABOVE INDICES (1 - 6): ")
        # choice 4: return a book
        elif choice == '4':
            UI.clear()
            Book.returnBack()
            UI.clear()  # clear screen
            UI.homePage()
            choice = input("PLEASE TYPE IN ONE OF THE ABOVE INDICES (1 - 6): ")
        # choice 5: delete a book
        elif choice == '5':
            UI.clear()
            Book.delete()
            UI.clear()  # clear screen
            UI.homePage()
            choice = input("PLEASE TYPE IN ONE OF THE ABOVE INDICES (1 - 6): ")
        # choice 6: exit
        elif choice == '6':
            exitAnswer = input("\nAre you sure to exit? Type Y/N: ")
            while exitAnswer != 'Y' and exitAnswer != 'N':
                exitAnswer = input("\nINVALID INPUT\nPLEASE TYPE Y/N: ")
            if exitAnswer == 'Y':
                print("\nThanks for visiting Gan's Library, goodbye!\n")
                exit(0)
            else:
                UI.clear()
                UI.homePage()
                choice = input("PLEASE TYPE IN ONE OF THE ABOVE INDICES (1 - 6): ")
        # invalid input
        else:
            choice = input("\nINVALID INDEX\nPLEASE TYPE IN A NUMBER BETWEEN 1 TO 6: ")
