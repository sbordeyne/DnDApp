'''
This module is the client class for client mode.
In the game we have the option of being a client or a host.
If client is selected, this module will be invoked. It is threaded
so it won't lock up the UI. It also uses UDP since I read somewhere
that UDP is good for games. It won't do any varification for the sent
data. It is fire and forget. The only exception is the 'ping'
command, which will be used to verify that the host is still present
every several seconds
'''
import socket
import sys
import threading
from queue import Queue


class client_thread(threading.Thread):
    '''
    This is the main client thread. Unlike the host, we only need one
    network IO thread as a client.
    '''
    def __init__(self, host, port, in_queue, out_queue):
        threading.Thread.__init__(self)
        # Create a TCP socket        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_address = (host, port)
        self.input_queue = in_queue
        self.out_queue = out_queue
        self.running = True
        
    def connect(self):
        self.sock.connect(self.server_address)

    def send(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
            

    def run(self):
        '''
        Run in a loop parsing data from input queue.
        Special input will responf with test, or kill
        the thread.

        The test response it to let the unittest know that
        the in/out queues are running. The kill test is to teminate
        the thread.

        .. note:: It's good practice to use thread.join() after sending
        the kill signal to prevent rogue threads.

        '''
        
        while self.running:
            try:
                data = self.input_queue.get()
                if data == 'test':
                    self.out_queue.put(data)
                elif data == 'et tu, Brute?':
                    self.running = False
                else:
                    self.connect()
                    self.send(data.encode())
                    #pass
                    

                # after parsing through the options mark queue task done
                self.input_queue.task_done()

            # I want this client thread to run continiously untill the kill
            # signal is sent or the host disconnects. So on an empty input
            # queue we will just chill out.
            except Exception as e:
                print(e)
                self.close()   # close socket on exeption
        self.close()     # close the socket after exiting the loop

    def close(self):
        print('closing socket')
        self.sock.close()
