import socket
from _thread import *


WELCOME_MESSAGE = "Hello, welcome to my chat ..."
NAME_REQUEST = "Please enter your name\n"
PHONE_REQUEST = "Please enter your phone number\n"
AGE_REQUEST = "Please enter your age\n"
ID_REQUEST = "Please enter your id\n"
MENU = "Please choose your option:\n1) New chat\n2) Join chat"

client = socket.socket()

# Try to connect.
while True:
    try:
        client.connect(('127.0.0.1', 8080))
        break
    except ConnectionRefusedError as e:
        pass
    except OSError as e:
        pass

# choose option
print(WELCOME_MESSAGE)


def get_message(conn):
    while True:
        print(conn.recv(1024).decode())


start_new_thread(get_message, (client,))

while True:
    message = input()

    client.send(message.encode())
