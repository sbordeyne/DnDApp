import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print ('starting server')
sock.bind(server_address)

while True:
    print ('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)
    
    print ('received {} from client'.format(len(data)) )
    print ( str(data))
    
    if data:
        sent = sock.sendto(data, address)
        print ('sending back')
