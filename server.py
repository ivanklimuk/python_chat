from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import logging
import datetime as dt
from constants import *

logging.basicConfig(level=logging.CRITICAL, format=LOG_FORMAT)
log = logging.getLogger(__name__)
log.setLevel(LOG_LEVEL)

clients = {}
addresses = {}

def accept_incoming_connections():
    """
    A handler for all new incoming connections.
    """
    while True:
        client, client_address = SERVER.accept()
        log.info('{} has connected.'.format(client_address))
        client.send(bytes('This is a public chat room.' + 'Type in your name and press enter to start!', 'utf8'))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    """
    A handler for each single client.
    """
    username = client.recv(BUFSIZ).decode('utf8')
    client.send(bytes('Welcome {}! If you ever want to quit, type "exit" to leave.'.format(username), 'utf8'))
    broadcast(bytes('{} has joined the chat!'.format(username), 'utf8'))
    log.info('{} joined the chat'.format(username))
    clients[client] = username
    while True:
        message = client.recv(BUFSIZ)
        if message != bytes('exit', 'utf8'):
            broadcast('[{}]-[{}]-"{}"'.format(dt.datetime.now(), username, message))
        else:
            client.send(bytes('exit', 'utf8'))
            client.close()
            del clients[client]
            broadcast(bytes('{} has left the chat.'.format(username), 'utf8'))
            break

def broadcast(message):
    """
    Broadcasts a message to all the clients.
    """
    for socket in clients:
        socket.send(bytes(message, 'utf8'))

def main():
    SERVER = socket(AF_INET, SOCK_STREAM)
    SERVER.bind((HOST, PORT))
    SERVER.listen(MAX_CONNECTIONS)
    log.info('Waiting for connection...')
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.join()
    SERVER.close()

if __name__ == '__main__':
    main()
