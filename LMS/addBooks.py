# the addBooks function related microservices for LMS version 1.0

import json
from tkinter import *


def submit(name, location, cat):
    with open('books.json', 'r') as infile:
        books = json.load(infile)
    status = "On Shelf at " + location
    books['number'] += 1
    index = books['number']
    books['member'][index] = {'name': name,
                              'location': location,
                              'status': status,
                              'category': cat}
    with open('books.json', 'w') as outfile:
        json.dump(books, outfile, indent=4)

    update = Tk()
    update.title("System Message")
    update.geometry("240x160")

    message = "\nSystem updated successfully!\nBook: " +\
              name + "\nis No. " + str(index) + " in the system.\n"
    mess = Label(update, text=message, font=('times new roman', 15))
    mess.grid(row=0, column=0, padx=20)
    close = Button(update, text="Close this window",
                   command=update.destroy,
                   font=('times new roman', 18))
    close.grid(row=1, column=0, padx=20, pady=10,
               ipadx=25, ipady=10)
    update.mainloop()


def addBook():
    root = Tk()
    root.title("Add a Book")
    root.geometry("960x600")
    cat = ["Computer Science", "Mathematics",
           "Economics", "Religious", "Fictions", "Manga"]

    category = StringVar(root)
    category.set("Please make a selection from below categories")

    # Label
    welcome = Label(root, text="Welcome to Gan's Library",
                    font=('times new roman', 80), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=2, padx=45,
                 pady=20)
    nameLabel = Label(root, text="Please type in the book's name:",
                      font=('times new roman', 18))
    nameLabel.grid(row=1, column=0, pady=20)
    locationLabel = Label(root, text="What's the location of this book?",
                          font=('times new roman', 18))
    locationLabel.grid(row=2, column=0, pady=20)
    categoryLabel = Label(root, text="Which category is this book?",
                          font=('times new roman', 18))
    categoryLabel.grid(row=3, column=0, pady=20)

    # text box
    name = Entry(root, width=40)
    name.grid(row=1, column=1)
    location = Entry(root, width=40)
    location.grid(row=2, column=1)
    categoryBox = OptionMenu(root, category, *cat)
    categoryBox.grid(row=3, column=1)

    # button
    submitB = Button(root, text="SUBMIT",
                     command=lambda: submit(name.get(),
                                            location.get(),
                                            category.get()),
                     font=('times new roman', 18))
    submitB.grid(row=4, column=1,
                 pady=10, ipadx=90, ipady=20)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('times new roman', 36))
    terminate.grid(row=5, column=0, columnspan=2,
                   pady=10, ipadx=90, ipady=20)
    root.mainloop()
