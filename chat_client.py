import socket
from _thread import *


WELCOME_MESSAGE = "Hello, welcome to my chat ..."
NAME_REQUEST = "Please enter your name\n"
PHONE_REQUEST = "Please enter your phone number\n"
AGE_REQUEST = "Please enter your age\n"
ID_REQUEST = "Please enter your id\n"
MENU = "Please choose your option:\n1) New chat\n2) Join chat"

print(WELCOME_MESSAGE)
user_name = input(NAME_REQUEST)
user_phone = input(PHONE_REQUEST)
user_age = input(AGE_REQUEST)
user_id = input(ID_REQUEST)


client = socket.socket()
client.connect(('127.0.0.1', 8080))


def get_message(conn):
    while True:
        print(conn.recv(1024).decode())


start_new_thread(get_message, (client,))

while True:
    message = input()

    client.send(message.encode())
