import socket
import threading
from queue import Queue
import sys

    
class server_thread(threading.Thread):
    
    def __init__(self, host, port, ctl_queue,out_queue):
        threading.Thread.__init__(self)
    
        if type(host) is not str:
            raise TypeError('host must be  string')
        if type(port) is not int:
            raise TypeError('port must be type int')
        if port > 99999 or port < 0 :
            raise ValueError('port must be between 0 and 9999')
        self.port = port
        self.host = host
        self.ctl_queue = ctl_queue
        self.out_queue = out_queue
        self.running = True
    
    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        
        print("Server loop running in thread:", server_thread.name)
        
        while self.running:
            # listen
            server.listen(1)
            self.out_queue.put("ready")            
            conn, addr = server.accept()
            print('Connected by', addr)
            # get data
            while True:
                data = conn.recv(1024)
                if not data: break
                self.out_queue.put("{}:{}".format(addr, data.decode()))
                
            try:
                # check for commands coming from ctl_queue
                command = self.ctl_queue.get()
                if command == 'kill':
                    print("{}: got kill command".format(server_thread.name))
                    self.running = False
                else:
                    pass
                self.ctl_queue.task_done()
            except Exception:
                print("Error")
            conn.close()

        print('server exiting')
        server.close()
