import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

init()

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
          Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
          Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
          Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

client_color = random.choice(colors)

HOST = '68.183.65.228'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'[*] Connecting to {HOST}:{PORT} ...')
s.connect((HOST, PORT))
print(f'[+] Connected')

name = input('Input your name')


def listen_message():
    while True:
        ms = s.recv(1024).decode()
        print('\n' + ms)


t = Thread(target=listen_message)
t.daemon = True
t.start()

while True:
    to_send = input('---> ')
    if to_send.lower() == 'exit':
        break

    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f'{client_color}[{date_now}] {name}: {to_send}{Fore.RESET}'
    s.send(to_send.encode())

s.connect()