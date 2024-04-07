# application d'envoi des messages

import socket

s = socket.socket()
host = input(str('Enter hostname or host IP : '))
port = 8080
s.connect((host, port))
print('Connecter au server')
while 1:
    message_entrant = s.recv(1024)
     message_entrant= message_entrant.decode()
    print(' Server : ', message_entrant)
    print()
    message = input(str('>> '))
    message = message.encode()
    s.send(message)
    print('envoyer')
    print()
