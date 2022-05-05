import socket

HOST = "127.0.0.1"
PORT = 65432


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024)
            if data == b'exit':
                break
            print(data.decode('utf-8'))
            reply = input()
            b = reply.encode()
            s.sendall(b)


if __name__ == '__main__':
    client()
