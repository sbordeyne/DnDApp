import unittest
import sys
from udp_client import client_thread
from queue import Queue

class networking_udp_client_Tests(unittest.TestCase):
    def setUp(self):
        self.in_q = Queue()
        self.out_q = Queue()
        self.host = 'localhost'
        self.port = 10000
        
    def test_start_client(self):
        '''
        Test to make a client object, run send a couple of signals then 
        quite. No real tests, just fist step to catch general exceptions
        and any othe misc runtime errors. 
        '''
        client = client_thread(self.host,
            self.port, self.in_q, self.out_q)
        #client.setDaemon(True)
        client.start()
        self.in_q.put('test')
        print(self.out_q.get())
        self.in_q.put('et tu, Brute?')
        client.join()

    def test_client_ping_through_io_queue(self):
        '''
        Create clientobject. Start running, send special 'test' signal in
        input queue and fail unless 'test' is present in output queue.
        The client should respond with 'test'.
        '''
        client = client_thread(self.host,
            self.port, self.in_q, self.out_q)
        client.start()
        self.in_q.put('test')
        response = self.out_q.get()
        self.failUnless(response == 'test')
        self.failIf(response == '')
        # now kill it
        self.in_q.put('et tu, Brute?')
        client.join()
        
    def test_client_close_on_kill_sig(self):
        client = client_thread(self.host,
            self.port, self.in_q, self.out_q)
        client.start()     
        self.in_q.put('et tu, Brute?')
        client.join()
        
    def test_client_eats_input_queue(self):
        '''
        Put something in the input queue to the client and fail unless the 
        the queue is empty. I.e. the client needs to eat the queue.
        '''
        client = client_thread(self.host,
            self.port, self.in_q, self.out_q)
        client.daemon = True
        client.start()
        self.in_q.put('test')
        self.in_q.put('test')
        self.in_q.put('test')
        self.in_q.put('test')
        # join the queue
        self.in_q.join()
        self.failUnless(self.in_q.empty())
        # now kill the client
        self.in_q.put('et tu, Brute?')
        client.join()


if __name__ == "__main__":

    client_test = unittest.TestLoader().loadTestsFromTestCase(networking_udp_client_Tests)
    alltest = unittest.TestSuite([client_test])


    result = unittest.TextTestRunner(verbosity=2).run(alltest) 
    if result.errors != []:
        sys.exit('test errors\n')
    if result.failures != []:
        sys.exit('test failures\n')
