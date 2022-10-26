"""

The main server holding the connection with each client using socket base on TCP protocol.

"""

import socket
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.SOCK_STREAM set the protocol to TCP. (Better for chat)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_address = ''
Port = 8080

"""
binds the server to an entered IP address and at the
specified port number.
The client must be aware of these parameters
"""
server.bind((IP_address, Port))

"""
listens for 10 active connections. This number can be
increased as per convenience.
"""
server.listen(10)

list_of_clients = []


def client_thread(conn, addr):

    # sends a message to the client whose user object is conn
    message = "Welcome to this chatroom!"
    conn.send(message.encode())

    while True:
        try:
            message = conn.recv(1024).decode()
            if message:

                """prints the message and address of the
                user who just sent the message on the server
                terminal"""
                print("<" + addr[0] + "> " + message)

                # Calls broadcast function to send message to all
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)

            else:
                """message may have no content if the connection
                is broken, in this case we remove the connection"""
                remove(conn)

        except:
            continue


"""Using the below function, we broadcast the message to all
clients who's object is not the same as the one sending
the message """


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()

                # if the link is broken, we remove the client
                remove(clients)


"""The following function simply removes the object
from the list that was created at the beginning of
the program"""


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:

    """Accepts a connection request and stores two parameters,
    conn: the socket object for that user
    addr: contains the IP address of that client we just connected.
    
    note connection is made with the three-way handshake to ensure the connection."""
    conn, addr = server.accept()

    """Maintains a list of clients for ease of broadcasting
    a message to all available people in the chatroom"""
    list_of_clients.append(conn)

    # prints the address of the user that just connected
    print(addr[0] + " connected")

    # creates and individual thread for every user
    # that connects
    start_new_thread(client_thread, (conn, addr))

conn.close()
server.close()

# TODO: use server.sendall() - send all size
