# Author: Gan Li
# Project: Personal Library Management System
# Version: 0.1 Minimum Viable Product
# Course: CS 361
# File Description: This is book management system file
# Functions: listByCategory(), search(), borrow(), returnBack(), manage()
import json

import UI


def listByCategory():
    category = input("PLEASE TYPE IN ONE OF THE ABOVE INDICES (1 - 6): ")
    if category == '1':
        cat = "Computer Science"
    elif category == '2':
        cat = "Mathematics"
    elif category == '3':
        cat = "Economics"
    elif category == '4':
        cat = "Religious"
    elif category == '5':
        cat = "Fictions"
    elif category == '6':
        cat = "Manga"
    else:
        print("INVALID INPUT\n")
        return
    UI.clear()  # clear the screen
    print("For", cat, "category, we have:")
    with open('books.json', 'r') as infile:
        books = json.load(infile)
    for book in books['member']:
        if books['member'][book]['category'] == cat:
            print('\t', book, '. ', books['member'][book]['name'], '\n\t----',
                  books['member'][book]['status'], sep='')
    print("\n")
    return


def add():
    with open('books.json', 'r') as infile:
        books = json.load(infile)
    print("\nPlease type in the book's name:\n")
    name = input()
    print("\nWhat's the location of this book?\n")
    location = input()
    print("\nWhich category is this book?\n")
    cat = input()
    status = "On Shelf at " + location
    books['number'] += 1
    index = books['number']
    books['member'][index] = {'name': name,
                              'location': location,
                              'status': status,
                              'category': cat}
    with open('books.json', 'w') as outfile:
        json.dump(books, outfile, indent=4)
    print("\nSystem updated successfully!\nBook",
          name, "is No.", index, "in the system.\n")


def borrow():
    with open('books.json', 'r') as infile:
        books = json.load(infile)
    print("\nDo you know the index number of the book you want to borrow?")
    index = input("If yes, type in the number here; if no, type 0: ")
    if index == '0':
        print("\nPlease go back to home page to view the book list to find the index number.\n")
    elif index in books['member']:
        if books['member'][index]['status'] == 'Book Borrowed':
            print("\nI am sorry, the book is currently borrowed by other people.\n")
        elif books['member'][index]['status'] == 'DELETED':
            print("\nI am sorry, the book is no longer available.\n")
        else:
            books['member'][index]['status'] = 'Book Borrowed'
            with open('books.json', 'w') as outfile:
                json.dump(books, outfile, indent=4)
            print("\nYou successfully borrowed the book.\nBook status updated.\n")
    else:
        print("\nINVALID INPUT\nThe index number does not exist.")
        borrow()
        return
    print("\nDo you want to borrow another book?")
    borrowAnswer = input("Please type in Y/N: ")
    while borrowAnswer != 'Y' and borrowAnswer != 'N':
        borrowAnswer = input("INVALID INPUT\nPlease type in Y/N: ")
    if borrowAnswer == 'Y':
        borrow()
    else:
        return


def returnBack():
    with open('books.json', 'r') as infile:
        books = json.load(infile)
    print("\nDo you know the index number of the book you want to return?")
    index = input("If yes, type in the number here; if no, type 0: ")
    if index == '0':
        print("\nPlease go back to home page to view the book list to find the index number.\n")
    elif index in books['member']:
        if books['member'][index]['status'] == 'Book Borrowed':
            books['member'][index]['location'] = input("\nPlease tell me the location where you put the book:\n")
            books['member'][index]['status'] = "On Shelf at " + books['member'][index]['location']
            with open('books.json', 'w') as outfile:
                json.dump(books, outfile, indent=4)
            print("\nYou successfully returned the book.\nBook status updated.\n")
        else:
            print("\nAre you sure you entered correct information?"
                  "\nThe book which matches the index number was not borrowed.\n")
    else:
        print("\nINVALID INPUT\nThe index number does not exist.")
        returnBack()
        return
    print("\nDo you want to return another book?")
    returnAnswer = input("Please type in Y/N: ")
    while returnAnswer != 'Y' and returnAnswer != 'N':
        returnAnswer = input("INVALID INPUT\nPlease type in Y/N: ")
    if returnAnswer == 'Y':
        returnBack()
    else:
        return


def delete():
    with open('books.json', 'r') as infile:
        books = json.load(infile)
    print("\nDo you know the index number of the book you want to delete from the library?")
    index = input("If yes, type in the number here; if no, type 0: ")
    if index == '0':
        print("\nPlease go back to home page to view the book list to find the index number.\n")
    elif index in books['member']:
        if books['member'][index]['status'] == 'DELETED':
            print("\nThe book status is already deleted in the system.\n")
        else:
            finalCheck = input("\nI have found the book.\nAre you sure you want to delete it?\n"
                               "Type in Y/N here: ")
            while finalCheck != 'Y' and finalCheck != 'N':
                finalCheck = input("\nINVALID INPUT\nPlease type in Y/N: ")
            if finalCheck == 'Y':
                books['member'][index]['status'] = 'DELETED'
                with open('books.json', 'w') as outfile:
                    json.dump(books, outfile, indent=4)
                print("\nYou successfully deleted the book.\nBook status updated.\n")
    else:
        print("\nINVALID INPUT\nThe index number does not exist.")
        delete()
        return
    print("\nDo you want to delete another book?")
    deleteAnswer = input("Please type in Y/N: ")
    while deleteAnswer != 'Y' and deleteAnswer != 'N':
        deleteAnswer = input("INVALID INPUT\nPlease type in Y/N: ")
    if deleteAnswer == 'Y':
        delete()
    else:
        return
