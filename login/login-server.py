import socket
import json

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # (HOST, PORT) is a tuple
    s.listen()

    while True:
        conn, addr = s.accept()
        print("Connected by ", addr)
        conn.sendall(b"CHOOSE WHAT YOU WANT TO DO:\n\t1. Log in\n\t2. Sign up\n")
        data = conn.recv(1024)
            
        if data == b'1':
            conn.sendall(b"\nPLEASE TYPE IN YOUR USERNAME: ")
            data = conn.recv(1024)
            with open('user-data.json', 'r') as infile:
                users = json.load(infile)
            username = data.decode('utf-8')
            if username not in users:
                conn.sendall(b"INVALID USERNAME\nType in anything to exit")
                data = b'exit'  # to end this process
            else:
                conn.sendall(b"\nPLEASE TYPE IN YOUR PASSWORD: ")
                data = conn.recv(1024)
                password = data.decode('utf-8')
                if users[username] == password:
                    conn.sendall(b"\nWelcome!\nThe rest of this project will be added, Type in anything to exit")
                    # initiate the following project here
                    data = b'exit'  # to end this process
                else:
                    conn.sendall(b"INCORRECT PASSWORD\nType in anything to exit")
                    data = b'exit'  # to end this process
        elif data == b'2':
            conn.sendall(b"\nPLEASE CREATE A NEW USERNAME: ")
            data = conn.recv(1024)
            username = data.decode('utf-8')
            with open('user-data.json', 'r') as infile:
                users = json.load(infile)
            while username in users:
                conn.sendall(b"\nTHE USERNAME ALREADY EXISTS\nPLEASE CREATE A NEW USERNAME: ")
                conn.recv(1024)
                username = data.decode('utf-8')
                
            conn.sendall(b"\nPLEASE CREATE A PASSWORD: ")
            data = conn.recv(1024)
            password = data.decode('utf-8')
            conn.sendall(b"\nPLEASE RE-ENTER THE SAME PASSWORD: ")
            data = conn.recv(1024)
            password2 = data.decode('utf-8')
            while password != password2:
                conn.sendall(b"\nPASSWORDS DO NOT MATCH\nPLEASE CREATE A PASSWORD: ")
                data = conn.recv(1024)
                password = data.decode('utf-8')
                conn.sendall(b"\nPLEASE RE-ENTER THE SAME PASSWORD: ")
                data = conn.recv(1024)
                password2 = data.decode('utf-8')
            users[username] = password
            with open('user-data.json', 'w') as outfile:
                json.dump(users, outfile, indent=4)
            conn.sendall(b"ACCOUNT CREATED\nWelcome!\nThe rest of this project will be added, Type in anything to exit")
            # continue the following project here
            data = b'exit'  # to end this process
        else:
            data = b'exit'
        trash = conn.recv(1024)
        conn.sendall(data)
        conn.close()
        