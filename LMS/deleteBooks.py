# the deleteBooks function related microservices for LMS version 1.0

import json
from tkinter import *


def checkDeletion(index):
    term = Tk()
    term.title("Delete?")
    term.geometry("360x160")

    prompt = Label(term, text="Are you sure to delete it?",
                   font=('times new roman', 24), anchor=CENTER)
    prompt.grid(row=0, column=0, columnspan=2, padx=45,
                pady=20)

    yes = Button(term, text="Yes",
                 command=lambda: delete(index),
                 font=('times new roman', 18))
    yes.grid(row=1, column=0, pady=10,
             ipadx=25, ipady=10)

    no = Button(term, text="No",
                command=term.destroy,
                font=('times new roman', 18))
    no.grid(row=1, column=1, pady=10,
            ipadx=25, ipady=10)
    term.mainloop()


def delete(index):
    with open('books.json', 'r') as infile:
        books = json.load(infile)

    if index in books['member']:
        if books['member'][index]['status'] == 'DELETED':
            message = "\nThe book's status is already \ndeleted in the system.\n"
        else:
            books['member'][index]['status'] = 'DELETED'
            with open('books.json', 'w') as outfile:
                json.dump(books, outfile, indent=4)
            message = "\nYou successfully deleted the book.\nBook status updated.\n"
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


def deleteBook():
    root = Tk()
    root.title("Delete a Book")
    root.geometry("480x300")
    prompt = Label(root, text="Please type in the book's index: ",
                   font=('times new roman', 18), anchor=CENTER)
    prompt.grid(row=0, column=0, padx=40, pady=40)
    index = Entry(root, width=10)
    index.grid(row=0, column=1)

    submitB = Button(root, text="SUBMIT",
                     command=lambda: delete(index.get()),
                     font=('times new roman', 18))
    submitB.grid(row=1, column=1,
                 pady=10, ipadx=20, ipady=10)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('times new roman', 24))
    terminate.grid(row=2, column=0, columnspan=2,
                   pady=10, ipadx=20, ipady=10)
    root.mainloop()
