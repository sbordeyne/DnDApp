import socket
import sys
import threading
from queue import Queue


class client_thread(threading.Thread):
    def __init__(self, host, port, in_queue, out_queue):
        threading.Thread.__init__(self) 
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = (host, port)
        self.input_queue = in_queue
        self.out_queue = out_queue
        self.running = True
        
    def send_ping(self):
        message = 'ping'.encode()
        try:
            # Send data
            print ('sending {}'.format(message))
            sent = sock.sendto(message, server_address)

            # Receive response
            print ('waiting to receive')
            data, server = sock.recvfrom(4096)
            print ('received {}'.format(data))
            
        except Exception:
            raise Exception

    def run(self):
        '''
        Run in a loop parsing data from input queue.
        Special input will responf with test, or kill
        the thread.
        '''
        while self.running:
            try:
                data = self.input_queue.get()
                if data == 'test':
                    self.out_queue.put(data)
                if data == 'et tu, Brute?':
                    self.running = False
            except queue.Empty:
                pass

    def close(self):
        print ('closing socket')
        sock.close()
