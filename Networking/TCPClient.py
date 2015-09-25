from socket import *

HOST = 'localhost'
PORT = 21567
ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.connect(ADDR)

while True:
    data = raw_input('Enter [blank to exit]>:')
    if not data:
        break

    tcpSocket.send(data)
    data = tcpSocket.recv(BUFSIZE)
    if not data:
        print 'No data received...exiting.'
        break
    print 'Response:', data

tcpSocket.close()
print 'Client exited...'
