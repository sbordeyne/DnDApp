import socketserver
import threading
from queue import Queue
import sys

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
    
class server_thread(threading.Thread):
    
    def __init__(self, host, port, queue):
        threading.Thread.__init__(self)
    
        if type(host) is not str:
            raise TypeError('host must be  string')
        if type(port) is not int:
            raise TypeError('port must be type int')
        if port > 99999 or port < 0 :
            raise ValueError('port must be between 0 and 9999')
        self.port = port
        self.host = host
        self.queue = queue
        self.running = True
    
    def run(self):
        server = ThreadedTCPServer((self.host, self.port), ThreadedTCPRequestHandler)
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)
        
        while self.running:
            try:
                data = self.queue.get()
                if data == 'kill':
                    self.running = False
                else:
                    pass
            except Exception:
                pass

        print('server exiting')
        server.shutdown()
        server.server_close()
