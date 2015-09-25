from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(ADDR)
tcpSocket.listen(5)

while True:
    print 'Waiting for connection...'
    tcpCSocket, addr = tcpSocket.accept()
    print '...connected from:', addr

    while True:
        data = tcpCSocket.recv(BUFSIZE)
        if not data:
            break
        tcpCSocket.send('[%s]:%s' % (ctime(), data))

    tcpCSocket.close()
    if not data:
        print 'Received shutdown command...exiting'
        break
tcpSocket.close()
