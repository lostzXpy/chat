import threading
import socket
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []


def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle clients'connections


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'\033[1;31m{alias}\033[m Saiu do chat! '.encode('utf-8'))
            aliases.remove(alias)
            break
# Main function to receive the clients connection


def receive():
    while True:
        print('Servidor ligado,esperando por usuários...')
        client, address = server.accept()
        print(f'Conexão estabelecida por {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'\033[1;31m{alias}\033[m Entrou no chat! '.encode('utf-8'))
        client.send('Você está conectado '.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
