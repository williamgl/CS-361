# the recommendation function related microservices for LMS version 0.3
# the related random number generator microservice is developed by my CS 361 teammate Evan Butler

# to make this function works, I modified Evan's code
# please check the commit to view Evan's source code

import json
import time
from tkinter import *


def RNG(book):
    with open('../Evan_microservice/prng-service.txt', 'w') as f:
        f.write(f"run\n{book}")
    time.sleep(1)
    with open('../Evan_microservice/prng-service.txt', 'r') as f:
        read_data = f.readline()
        if read_data == 'index\n':
            index = f.readline()
        else:
            index = '-1'
    return index


def randomRec():
    with open('books.json', 'r') as infile:
        books = json.load(infile)
    inventory = books['number']
    index = RNG(inventory)

    RR = Tk()
    RR.title("Recommendation")
    RR.geometry("960x600")

    welcome = Label(RR, text="Welcome to Gan's Library",
                    font=('times new roman', 80), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=2, padx=45,
                 pady=20)

    if index == '-1':
        errorLabel = Label(RR, text='Error: RNG Microservice is not initiated',
                           font=('times new roman', 48), anchor=CENTER)
        errorLabel.grid(row=1, column=0, columnspan=2, padx=45,
                        pady=20)
    else:
        name = books['member'][index]['name']
        location = books['member'][index]['location']
        status = books['member'][index]['status']
        category = books['member'][index]['category']
        dataLabel = Label(RR, text=f'Book index:\n'
                                   f'Book name:\n'
                                   f'Book location:\n'
                                   f'Book category:\n'
                                   f'Book status:',
                          font=('times new roman', 24), anchor='w',
                          justify=LEFT)
        dataLabel.grid(row=2, column=0, pady=10, ipadx=25, ipady=20)
        contentLabel = Label(RR, text=f'{index}\n'
                                      f'{name}\n'
                                      f'{location}\n'
                                      f'{category}\n'
                                      f'{status}',
                             font=('times new roman', 24), anchor='w',
                             justify=LEFT)
        contentLabel.grid(row=2, column=1, pady=10, ipadx=25, ipady=20)

    terminate = Button(RR, text="Close This Window", command=RR.destroy,
                       font=('times new roman', 36))
    terminate.grid(row=5, column=0, columnspan=2,
                   pady=10, ipadx=90, ipady=20)
    RR.mainloop()
