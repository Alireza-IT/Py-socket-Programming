import socket
import threading  # create multiple thread with one python program
import time

HEADER = 64
# first define port for server
PORT = 5050
#SERVER = "localhost"
SERVER = socket.gethostbyname(socket.gethostname())  # get ip automatically
ADDR = (SERVER, PORT)  # bind socket to address need to be in tuple
# make socket and allow connection and pick socket and bind socket to address to define what type of ip we are working on
# make socket and define category and streaming data through the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#fmaliy and type
DISCONNECT_MESSAGE = "!DISCONNECT"
# bind this to addres
server.bind(ADDR)
FORMAT = 'utf-8'


def handle_client(conn, addr):  # handle all communication between server and client
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        # how many byte we nexpect to recive from the client so wait on socket to recive somethings
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # how byte needs to get ? and decode to string again
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            # send from server to client
            conn.send("Msg recieved".encode(FORMAT))
    conn.close()


# start connection
def start():  # allow server to listen to connection and pass to handel connection
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        # wait for new connection to server and store into socket obj and add is information of connection
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # show number of active thread on this process (number of client) because we have main thread wich is  start thread
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")


print("[STARTING] server is starting....")
start()
