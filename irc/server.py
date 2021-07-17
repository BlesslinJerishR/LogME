# Run me first
import socket
import select

# Constants
HEADER_LENGTH = 10
# Ip and Port
IP = "127.0.0.1"
PORT = 1234

# Server Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# Binding
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf- 8').strip())
        return {"header": message_header,
                "data": client_socket.recv(message_length)
                }
    except:
        return False
        pass


def start_server():
    print(f"ip : {IP} \nport : {PORT}\nWaiting for connections ...")
    while True:
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
        for notified_socket in read_sockets:
            if notified_socket == server_socket:
                client_socket, client_address = server_socket.accept()
                user = receive_message(client_socket)
                if user is False:
                    continue
                sockets_list.append(client_socket)
                clients[client_socket] = user
                # Address
                # {client_address[0]} : {client_address[1]}
                print(" ")
                print(f"Accepted new connection\nUsername : {user['data'].decode('utf-8')}")
                print(f'{user["data"].decode("utf-8")} has joined the IRC Room')
                print(f'welcome to private IRC Chat Window {user["data"].decode("utf-8")}')
                print(" ")
            else:
                message = receive_message(notified_socket)
                if message is False:
                    print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                    print(f'{clients[notified_socket].decode("utf-8")} has left the IRC Room')
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue
                user = clients[notified_socket]

                print(f"{user['data'].decode('utf-8')} > {message['data'].decode('utf-8')}")

                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]


if __name__ == '__main__':
    start_server()
