import socket
from threading import *

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print(f'[*] Listening {HOST}:{PORT}')
client_sockets = set()


def listen_connection(connection):
    while True:
        try:
            data = connection.recv(1024).decode()
            for socket_ in client_sockets:
                socket_.send(data.encode())
        except:
            pass


def command():
    com = input()
    if com.upper() == 'Q':
        for i in client_sockets:
            i.close()
        s.close()


command_listen = Thread(target=command)
command_listen.daemon = True
command_listen.start()

loop = True
while loop:
    try:
        conn, addr = s.accept()
        print(f'[+] Client {addr} connected')
        client_sockets.add(conn)
        t = Thread(target=listen_connection, args=(conn,))
        t.daemon = True
        t.start()
    except:
        print('Server was stopped.')
        loop = False





