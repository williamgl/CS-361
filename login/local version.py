# Here is the basically local version of the login function
# It does not request and receive any data using socket as communication pipe

import json


def login():
    choice = input("CHOOSE WHAT YOU WANT TO DO:\n\t1. Log in\n\t2. Sign up\n")
    if choice == '1':
        username = input("\nPLEASE TYPE IN YOUR USERNAME: ")
        with open('user-data.json', 'r') as infile:
            users = json.load(infile)
        if username not in users:
            print("INVALID USERNAME\n")
        else:
            password = input("\nPLEASE TYPE IN YOUR PASSWORD: ")
            if users[username] == password:
                print(f"\nWelcome, {username}!\n")
                # initiate the following project here
                
            else:
                print("INCORRECT PASSWORD\n")
    elif choice == '2':
        username = input("\nPLEASE CREATE A NEW USERNAME: ")
        with open('user-data.json', 'r') as infile:
            users = json.load(infile)
        while username in users:
            print("\nTHE USERNAME ALREADY EXISTS")
            username = input("\nPLEASE CREATE A NEW USERNAME: ")
        password = input("\nPLEASE CREATE A PASSWORD: ")
        password2 = input("\nPLEASE RE-ENTER THE SAME PASSWORD: ")
        while password != password2:
            print("\nPASSWORDS DO NOT MATCH")
            password = input("\nPLEASE CREATE A PASSWORD: ")
            password2 = input("\nPLEASE RE-ENTER THE SAME PASSWORD: ")
        users[username] = password
        with open('user-data.json', 'w') as outfile:
            json.dump(users, outfile, indent=4)
        print(f"ACCOUNT CREATED\nWelcome, {username}")
        # continue the following project here
    else:
        print("INVALID INPUT\n")


if __name__ == '__main__':
    login()
