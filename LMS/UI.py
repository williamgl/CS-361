# Author: Gan Li
# Project: Personal Library Management System
# Version: 0.1 Minimum Viable Product
# Course: CS 361
# File Description: This is the user interface file of this project
from os import system, name


def homePage():
    print("CHOOSE WHAT YOU WANT TO DO:\n\n\t1. View the Book List by Category\n"
          "\t2. Add a Book\n\t3. Borrow a Book\n\t4. Return a Book\n"
          "\t5. Delete a Book\n\t6. Exit the Library\n")  # display options


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print("\t\t\t Welcome to Gan's Library\n")  # display title


def category():
    print("CHOOSE THE CATEGORY YOU ARE INTERESTED IN:\n\n\t1. Computer Science\n"
          "\t2. Mathematics\n\t3. Economics\n\t4. Religious\n"
          "\t5. Fictions\n\t6. Manga\n")
