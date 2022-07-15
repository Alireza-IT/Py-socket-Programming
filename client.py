import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)  # encode string to byte
    msg_length = len(message)
    # how much need to pass the msg to 64
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello world!")
send("Hello worldVodafone")
send("Hello worldTIM")
send("!DISCONNECT")
