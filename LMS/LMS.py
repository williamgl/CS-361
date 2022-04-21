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
import UI
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == '__main__':
    clear()  # clear screen
    UI.homePage()
