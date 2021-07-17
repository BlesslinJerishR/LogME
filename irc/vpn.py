import webbrowser
import time
from datetime import date
import datetime as dt
today = date.today()
year = dt.date.today().year

irc_file = f'Clogs/{year}/irc.txt'

# Tick Symbol
def tick():
    symbol = '\u2713'
    return symbol

def quit_irc():
    irc_menu()

def start_server_main():
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
                print(f"Accepted new connection")
                print(" ")
                print(f"Username : {user['data'].decode('utf-8')}")
                print(f'{user["data"].decode("utf-8")} has joined the IRC Room')
                print(f'welcome to private IRC Chat Window {user["data"].decode("utf-8")}')
                print(" ")

                with open(irc_file, 'a') as ia:
                    ia.write(f"\n{today}")
                    ia.write(f"\nUsername : {user['data'].decode('utf-8')}")
                    ia.write(f'\n{user["data"].decode("utf-8")} has joined the IRC Room')
                    ia.write(f'\nwelcome to private IRC Chat Window {user["data"].decode("utf-8")}')
            else:
                message = receive_message(notified_socket)
                if message is False:
                    print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                    print(f'{clients[notified_socket]["data"].decode("utf-8")} has left the IRC Room')
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue
                user = clients[notified_socket]
                print(f"{user['data'].decode('utf-8')} > {message['data'].decode('utf-8')}")
                with open(irc_file, 'a') as ia:
                    ia.write(f"\n{user['data'].decode('utf-8')} > {message['data'].decode('utf-8')}")
                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]


def start_client_main():
    # Run me second
    import socket
    import errno
    import signal
    timeout = None

    def irc_banner():
        print("""
                          ___           ___                    ___           ___           ___                 
            ___          /  /\         /  /\                  /  /\         /__/\         /  /\          ___   
           /  /\        /  /::\       /  /:/                 /  /:/         \  \:\       /  /::\        /  /\  
          /  /:/       /  /:/\:\     /  /:/                 /  /:/           \__\:\     /  /:/\:\      /  /:/  
         /__/::\      /  /:/~/:/    /  /:/  ___            /  /:/  ___   ___ /  /::\   /  /:/~/::\    /  /:/   
         \__\/\:\__  /__/:/ /:/___ /__/:/  /  /\          /__/:/  /  /\ /__/\  /:/\:\ /__/:/ /:/\:\  /  /::\   
            \  \:\/\ \  \:\/:::::/ \  \:\ /  /:/          \  \:\ /  /:/ \  \:\/:/__\/ \  \:\/:/__\/ /__/:/\:\  
             \__\::/  \  \::/~~~~   \  \:\  /:/            \  \:\  /:/   \  \::/       \  \::/      \__\/  \:\ 
             /__/:/    \  \:\        \  \:\/:/              \  \:\/:/     \  \:\        \  \:\           \  \:\\
             \__\/      \  \:\        \  \::/                \  \::/       \  \:\        \  \:\           \__\/
                         \__\/         \__\/                  \__\/         \__\/         \__\/                
""")
    def chat():
        inp = wait(f"{my_username} > ", "", 20, "")
        # auto refresh in 15 secs
        return inp

    def chat_refresh():
       inp = wait("refreshing...", "", 1, "")
       # quick refresh
       return inp

    def wait(text, default, time, timeoutDisplay = None, **kwargs):
        signal.signal(signal.SIGALRM, interrupt)
        signal.alarm(time) # sets timeout
        global timeout
        try:
            inp = input(text)
            signal.alarm(0)
            timeout = False
        except (KeyboardInterrupt):
            printInterrupt = kwargs.get("printInterrupt", True)
            if printInterrupt:
                print("Keyboard interrupt")
            timeout = True # Do this so you don't mistakenly get input when there is none
            inp = default
        except:
            timeout = True
            if not timeoutDisplay is None:
                print(timeoutDisplay)
            signal.alarm(0)
            inp = default
        return inp

    def interrupt(signum, frame):
        raise Exception("")

    HEADER_LENGTH = 10
    IP = "127.0.0.1"
    PORT = 1234

    irc_banner()
    my_username = input("Username : ")
    print(" ")
    print(f'{my_username} has joined the IRC Room')
    print(f'welcome to private IRC Chat Window {my_username}')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    client_socket.setblocking(False)
    username = my_username.encode('utf-8')
    username_header = f"{len(username) :< {HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(username_header + username)
    print("press 'r' to refresh chat room")
    print("press 'q' to quit chat room\n")
    print(" ")
    while True:
        message = chat()
        if message == 'r':
            chat_refresh()
        elif message == 'q':
            irc_menu()
        else:
            message = message.encode('utf-8')
            message_header = f"{len(message) :< {HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + message)
        try:
            while True:
                # receive things
                username_header = client_socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print(f"{my_username} has left the IRC Room")
                    print("Connection closed")

                username_length = int(username_header.decode('utf-8').strip())
                username = client_socket.recv(username_length).decode('utf-8')

                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                message = client_socket.recv(message_length).decode('utf-8')
                print(f"{username} > {message}")
        except IOError as e:
            if e.errno != errno.EAGAIN and errno != errno.EWOULDBLOCK:
                # print('Reading error', str(e))
                pass
        except Exception as e:
            # print('General error', str(e))
            pass

def i_chat():
    print("""
        After Installation,
        
        * import 'vpn.ovpn' file to open vpn 
        * click connect
        
        # Press 'i' for IRC chat window
        """)
    key = str(input(">> "))
    if key == 'i':
        irc_menu()
    else:
        print("Yo have eyes nigga ?")


def vpn():
    print("""
                                           ___         ___     
                              ___         /  /\       /__/\    
                             /__/\       /  /::\      \  \:\   
                             \  \:\     /  /:/\:\      \  \:\  
                              \  \:\   /  /:/~/:/  _____\__\:\ 
                          ___  \__\:\ /__/:/ /:/  /__/::::::::\\
                         /__/\ |  |:| \  \:\/:/   \  \:\~~\~~\/
                         \  \:\|  |:|  \  \::/     \  \:\  ~~~ 
                          \  \:\__|:|   \  \:\      \  \:\     
                           \__\::::/     \  \:\      \  \:\    
                               ~~~~       \__\/       \__\/    
    """)

    print("""
        1. Download and Install
        2. Guide
        """)
    key = int(input(">> ")) or str(input(">> "))
    if key == 1:
        print("Install OpenVpn")
        time.sleep(1)
        print("Opening Download page")
        time.sleep(1)
        ovpn = "https://openvpn.net/community-downloads/"
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open_new(ovpn)
        time.sleep(.5)
        i_chat()
    elif key == 2:
        i_chat()
    elif key == 'h':
        irc_menu()
    else:
        print("Yo have eyes nigga ?")

def irc_menu():
    print("""
                  ___           ___           ___                        ___           ___     
                 /  /\         /  /\         /  /\          ___         /  /\         /  /\    
                /  /:/_       /  /:/_       /  /::\        /__/\       /  /:/_       /  /::\   
               /  /:/ /\     /  /:/ /\     /  /:/\:\       \  \:\     /  /:/ /\     /  /:/\:\  
              /  /:/ /::\   /  /:/ /:/_   /  /:/~/:/        \  \:\   /  /:/ /:/_   /  /:/~/:/  
             /__/:/ /:/\:\ /__/:/ /:/ /\ /__/:/ /:/___  ___  \__\:\ /__/:/ /:/ /\ /__/:/ /:/___
             \  \:\/:/~/:/ \  \:\/:/ /:/ \  \:\/:::::/ /__/\ |  |:| \  \:\/:/ /:/ \  \:\/:::::/
              \  \::/ /:/   \  \::/ /:/   \  \::/~~~~  \  \:\|  |:|  \  \::/ /:/   \  \::/~~~~ 
               \__\/ /:/     \  \:\/:/     \  \:\       \  \:\__|:|   \  \:\/:/     \  \:\     
                 /__/:/       \  \::/       \  \:\       \__\::::/     \  \::/       \  \:\    
                 \__\/         \__\/         \__\/           ~~~~       \__\/         \__\/    
     
    1. Start Server
    2. IRC Chat""")
    key = int(input(">> "))
    if key == 1:
        time.sleep(2)
        print(f"Server started successfully {tick()}")
        time.sleep(2)
        print(f"Daemon tool running {tick()}")
        start_server_main()
    elif key == 2:
        start_client_main()
    else:
        print("Yo have eyes nigga ?")

if __name__ == '__main__':
    start_client_main()