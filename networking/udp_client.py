import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'.encode()

try:

    # Send data
    print ('sending {}'.format(message))
    sent = sock.sendto(message, server_address)

    # Receive response
    print ('waiting to receive')
    data, server = sock.recvfrom(4096)
    print ('received {}'.format(data))

finally:
    print ('closing socket')
    sock.close()
