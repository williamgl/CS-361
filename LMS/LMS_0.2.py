from tkinter import *
from viewBooks import listByCategory
from addBooks import addBook
from deleteBooks import deleteBook
from borrowBooks import borrowBook
from returnBooks import returnBook


def checkExit():
    term = Tk()
    term.title("Exit?")
    term.geometry("300x160")

    prompt = Label(term, text="Do you want to exit?",
                   font=('times new roman', 24), anchor=CENTER)
    prompt.grid(row=0, column=0, columnspan=2, padx=45,
                pady=20)

    yes = Button(term, text="Yes",
                 command=exit,
                 font=('times new roman', 18))
    yes.grid(row=1, column=0, pady=10,
             ipadx=25, ipady=10)

    no = Button(term, text="No",
                command=term.destroy,
                font=('times new roman', 18))
    no.grid(row=1, column=1, pady=10,
            ipadx=25, ipady=10)
    term.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.title("Gan's Library")
    root.geometry("960x600")

    # Labels
    welcome = Label(root, text="Welcome to Gan's Library",
                    font=('times new roman', 80), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=2, padx=45,
                 pady=20)

    # Buttons
    view = Button(root, text="View the Book List by Category", command=listByCategory,
                  font=('times new roman', 36))
    view.grid(row=1, column=0, columnspan=2, pady=10,
              ipadx=142, ipady=20)

    add = Button(root, text="Add a Book", command=addBook,
                 font=('times new roman', 36))
    add.grid(row=2, column=0, pady=10,
             ipadx=45, ipady=20)

    delete = Button(root, text="Delete a Book", command=deleteBook,
                    font=('times new roman', 36))
    delete.grid(row=2, column=1, pady=10,
                ipadx=45, ipady=20)

    borrow = Button(root, text="Borrow a Book", command=borrowBook,
                    font=('times new roman', 36))
    borrow.grid(row=3, column=0, pady=10,
                ipadx=21, ipady=20)

    returnB = Button(root, text="Return a Book", command=returnBook,
                     font=('times new roman', 36))
    returnB.grid(row=3, column=1, pady=10,
                 ipadx=43, ipady=20)

    terminate = Button(root, text="Exit", command=checkExit,
                       font=('times new roman', 36))
    terminate.grid(row=4, column=0, columnspan=2,
                   pady=10, ipadx=90, ipady=20)

    root.mainloop()
