import socketserver
import sys


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class 
    
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

class Host_Server(object):
    
    def __init__(self, host, port):
    
        if type(host) is not str:
            raise TypeError('host must be  string')
        if type(port) is not int:
            raise TypeError('port must be type int')
        if port > 99999 or port < 0 :
            raise ValueError('port must be between 0 and 9999')
    

        # Create the server
        server = socketserver.TCPServer((host, port), MyTCPHandler)

        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

h = Host_Server('localhost', 10000)

