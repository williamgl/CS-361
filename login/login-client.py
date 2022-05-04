import socket

HOST = "127.0.0.1"
PORT = 65432

message = b'A message from CS361 by client'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message)
    print(f"Message Sent: {message}")

    data = s.recv(1024)
    print(f"Message Received: {data}")
