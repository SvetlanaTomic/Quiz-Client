from socket import *
from threading import *


class ListenThread(Thread):
    def __init__(self, socket):
        self.socket = socket
        super().__init__()
        self.start()

    def run(self):
        # print("I can receive your messages")
        while True:
            try:
                message_from_server = self.socket.recv(1024).decode()

                if message_from_server == '':
                    print('Something went wrong, I am closing connection')
                    break

                if message_from_server == "CLOSE":
                    print('Server closed connection')
                    socket.close()
                    break
                else:
                    print(message_from_server)


            except ConnectionResetError:
                print('Server has some troubles running, connection will be closed')
                break
            except:
                print('Something went wrong, I am closing connection')
                break

        # ovde proveriti da li server zeli da prekine komunikaciju


serverName = 'localhost'
serverPort = 8090

# username = input("Enter your username ")

while True:
    try:
        socket = socket(AF_INET, SOCK_STREAM)

        socket.connect((serverName, serverPort))
        print("Successfully connected")
        # povezan je na server

        # socket.send(username.encode())

        listener = ListenThread(socket)
        # cim se jednom konektuje moze da zavrsi sa ovim delom
        break
    except OSError:
        print("Unable to connect to server")
        # dodati da li zali da pokusa opet
        break

while True:
    # ovde klijent unosi podatke i prekida komuniakciju ako zeli
    try:
        message = input()
        socket.send(message.encode())

    except OSError:
        print('Error while sending message')
