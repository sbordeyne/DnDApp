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
        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (host, port)
        self.input_queue = in_queue
        self.out_queue = out_queue
        self.running = True

    def send_ping(self):
        '''
        Send a special message "ping" to the host and listen
        for a reply. Later this will be used to verify that the host
        is still active be ping once every several seconds.
        '''
        message = 'ping'.encode()
        try:
            # Send data
            print('sending {}'.format(message))
            self.sock.sendto(message, self.server_address)

            # Receive response
            print('waiting to receive')
            data, server = self.sock.recvfrom(4096)
            print('received {}'.format(data))

        except Exception:
            raise Exception

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
                if data == 'et tu, Brute?':
                    self.running = False
                else:
                    #  Here is where I will later invoke the sending function
                    pass

                # after parsing through the options mark queue task done
                self.input_queue.task_done()

            # I want this client thread to run continiously untill the kill
            # signal is sent or the host disconnects. So on an empty input
            # queue we will just chill out.
            except self.input_queue.Empty:
                pass
        self.close()     # close the socket after exiting the loop

    def close(self):
        print('closing socket')
        self.sock.close()
