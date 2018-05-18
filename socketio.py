'''
Created on 17 May 2018

@author: mark
'''
from socket import socket
sock = socket()
#sock.connect(('katfs.kat.ac.za',25))
sock.connect(('localhost',10002))
try:
    while True:
        data = raw_input('> ')
        if data == 'quit':
            break
        sock.send(data+'\n')
        print sock.recv(4096)
finally:
    print "remote close"
    sock.close()    