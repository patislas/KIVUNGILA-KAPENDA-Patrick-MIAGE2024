# application qui accepte les requete des client

import socket

s = socket.socket()
host = socket.gethostname()
print(' le serveur demarre sur le host : ', host)
port = 8080
s.bind((host, port))
print()
print('attente de la connection')
print()
s.listen(1)
conn, addr = s.accept()
print(addr, ' est connecter au server')
print()
while 1:
    message = input(str('>> '))
    message = message.encode()
    conn.send(message)
    print('envoyer')
    print()
    message_entrant = conn.recv(1024)
    message_entrant = message_entrant.decode()
    print(' Client : ', message_entrant)
    print()
