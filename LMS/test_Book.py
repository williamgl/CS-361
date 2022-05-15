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
                      font=('times new roman', 15))
    nameLabel.grid(row=1, column=0, pady=20)
    locationLabel = Label(root, text="What's the location of this book?",
                          font=('times new roman', 15))
    locationLabel.grid(row=2, column=0, pady=20)
    categoryLabel = Label(root, text="Which category is this book?",
                          font=('times new roman', 15))
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
        message = "\nINVALID INPUT\nThe index number does not exist."

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


def borrowBook():
    pass


def returnBook():
    pass
