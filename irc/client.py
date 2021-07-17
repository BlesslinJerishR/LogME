def start_client():
    # Run me second
    import socket
    import errno
    import signal
    timeout = None

    def quit_irc():
        # irc_menu()
        pass
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
        inp = wait(f"{my_username} > ", "", 15, "")
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
    print("press 'q' to quit chat room")
    print(" ")
    while True:
        message = chat()
        if message == 'r':
            chat_refresh()
        elif message == 'q':
            quit_irc()
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


if __name__ == '__main__':
    start_client()
