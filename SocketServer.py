'''
Created on 17 May 2018

@author: mark
'''
from socket import socket

server_socket = socket()
try:
    server_socket.bind(('localhost',10002))
    server_socket.listen(6)
    (sock, address) = server_socket.accept()
    while True:
        line = sock.recv(4096)
        if line == 'quit':
            break
        sock.send(line + '\n')
finally:
    sock.close()