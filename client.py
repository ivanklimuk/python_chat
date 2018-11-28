from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from constants import *


def receive():
    """
    A handler for all received messages: receives the message and puts it
    into the message box.
    """
    while True:
        try:
            msg = CLIENT_SOCKET.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # in case the client has left the chat
            break

def send(event=None):
    """
    A handler for outgoing messages.
    """
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    CLIENT_SOCKET.send(bytes(msg, "utf8"))
    if msg == "exit":
        CLIENT_SOCKET.close()
        top.quit()

def on_closing(event=None):
    """
    This function is to be called when the window is closed.
    """
    my_msg.set("exit")
    send()

def build_client_window():
    """
    A wrapper for all actions which are necessary to draw the client UI window.
    """
    top = tkinter.Tk()
    top.title("Chat")

    messages_frame = tkinter.Frame(top)
    global my_msg
    my_msg = tkinter.StringVar()  # 'global' should not be used in the future
    my_msg.set("Type your messages here.")
    scrollbar = tkinter.Scrollbar(messages_frame)

    global msg_list
    msg_list = tkinter.Listbox(messages_frame,
                                      height=15,
                                      width=50,
                                      yscrollcommand=scrollbar.set)  # 'global' should not be used in the future
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msg_list.pack()
    messages_frame.pack()

    entry_field = tkinter.Entry(top, textvariable=my_msg)
    entry_field.bind("<Return>", send)
    entry_field.pack()
    send_button = tkinter.Button(top, text="Send", command=send)
    send_button.pack()

    top.protocol("WM_DELETE_WINDOW", on_closing)

def main():
    SERVER_HOST = input('Enter host (press "return" to leave the default value "{}"):'.format(HOST)) or HOST
    SERVER_PORT = int(input('Enter port(press "return" to leave the default value "{}"):'.format(PORT)) or PORT)

    global CLIENT_SOCKET
    CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
    CLIENT_SOCKET.connect((SERVER_HOST, SERVER_PORT))

    build_client_window()

    RECEIVE_THREAD = Thread(target=receive)
    RECEIVE_THREAD.start()
    tkinter.mainloop()  # starts GUI execution.

if __name__ == '__main__':
    main()
