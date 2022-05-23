# the borrowBooks function related microservices for LMS version 1.0

import json
from tkinter import *


def borrow(index):
    with open('books.json', 'r') as infile:
        books = json.load(infile)

    if index in books['member']:
        if books['member'][index]['status'] == 'Book Borrowed':
            message = "\nI am sorry.\nThe book is currently borrowed \nby another user.\n"
        elif books['member'][index]['status'] == 'DELETED':
            message = "\nI am sorry.\nThe book is no longer available.\n"
        else:
            books['member'][index]['status'] = 'Book Borrowed'
            with open('books.json', 'w') as outfile:
                json.dump(books, outfile, indent=4)
            message = "\nBook successfully borrowed!\nBook status updated.\n"
    else:
        message = "\nINVALID INPUT\nThe index number does not exist.\n"

    update = Tk()
    update.title("System Message")
    update.geometry("240x160")

    mess = Label(update, text=message, font=('times new roman', 15))
    mess.grid(row=0, column=0, padx=20)
    close = Button(update, text="Close this window",
                   command=update.destroy,
                   font=('times new roman', 18))
    close.grid(row=1, column=0, padx=20, pady=10,
               ipadx=25, ipady=10)
    update.mainloop()


def borrowBook():
    root = Tk()
    root.title("Borrow a Book")
    root.geometry("480x300")
    prompt = Label(root, text="Please type in the book's index: ",
                   font=('times new roman', 18), anchor=CENTER)
    prompt.grid(row=0, column=0, padx=40, pady=40)
    index = Entry(root, width=10)
    index.grid(row=0, column=1)

    submitB = Button(root, text="SUBMIT",
                     command=lambda: borrow(index.get()),
                     font=('times new roman', 18))
    submitB.grid(row=1, column=1,
                 pady=10, ipadx=20, ipady=10)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('times new roman', 24))
    terminate.grid(row=2, column=0, columnspan=2,
                   pady=10, ipadx=20, ipady=10)
    root.mainloop()
