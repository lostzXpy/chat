import threading
import socket
import os 

def clear():
    os.system('clear')
    
date = os.system('date')

clear()

a = '[\033[1;31mi\033[m]'
alias = input('oneLost CHAT\n{} Digite seu nickname: \033[1;31m'.format(a))
clear()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59003))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('\n\033[1;31mHouve um erro desconhecido\n')
            client.close()
            break


def client_send():
    while True:
        message = f'{date} | <\033[1;31m@{alias}\033[m> {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
