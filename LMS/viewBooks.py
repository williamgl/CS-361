# the viewBooks function related microservices for LMS version 0.2

import json
from tkinter import *


def view(cat):
    output = "For " + cat + " category, we have:\n"
    with open('books.json', 'r') as infile:
        books = json.load(infile)
    for book in books['member']:
        if books['member'][book]['category'] == cat:
            output += ('\t' + book + '. ' + books['member'][book]['name'] + '\n\t----' +
                       books['member'][book]['status'] + '\n')
    root = Tk()
    root.title(cat)
    root.geometry("960x1200")
    welcome = Label(root, text="Welcome to Gan's Library",
                    font=('times new roman', 80), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=2, padx=45,
                 pady=20)

    content = Label(root, text=output, font=('times new roman', 18),
                    anchor='w', justify=LEFT)
    content.grid(row=1, column=0, columnspan=2, pady=10,
                 ipadx=25, ipady=20)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('times new roman', 24))
    terminate.grid(row=4, column=0, columnspan=2,
                   pady=10, ipadx=90, ipady=20)

    root.mainloop()


def listByCategory():
    root = Tk()
    root.title("Categories")
    root.geometry("960x600")
    # Labels
    welcome = Label(root, text="Welcome to Gan's Library",
                    font=('times new roman', 80), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=2, padx=45,
                 pady=20)
    # Buttons
    CS = Button(root, text="Computer Science",
                command=lambda: view("Computer Science"),
                font=('times new roman', 36))
    CS.grid(row=1, column=0, pady=10,
            ipadx=10, ipady=20)

    math = Button(root, text="Mathematics",
                  command=lambda: view("Mathematics"),
                  font=('times new roman', 36))
    math.grid(row=1, column=1, pady=10,
              ipadx=45, ipady=20)

    econ = Button(root, text="Economics",
                  command=lambda: view("Economics"),
                  font=('times new roman', 36))
    econ.grid(row=2, column=0, pady=10,
              ipadx=62, ipady=20)

    religious = Button(root, text="Religious",
                       command=lambda: view("Religious"),
                       font=('times new roman', 36))
    religious.grid(row=2, column=1, pady=10,
                   ipadx=68, ipady=20)

    fictions = Button(root, text="Fictions",
                      command=lambda: view("Fictions"),
                      font=('times new roman', 36))
    fictions.grid(row=3, column=0, pady=10,
                  ipadx=83, ipady=20)

    manga = Button(root, text="Manga",
                   command=lambda: view("Manga"),
                   font=('times new roman', 36))
    manga.grid(row=3, column=1, pady=10,
               ipadx=88, ipady=20)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('times new roman', 36))
    terminate.grid(row=4, column=0, columnspan=2,
                   pady=10, ipadx=90, ipady=20)
    root.mainloop()
