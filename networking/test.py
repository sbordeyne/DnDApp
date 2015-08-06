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
        client = client_thread(self.host,
            self.port, self.in_q, self.out_q)
        #client.setDaemon(True)
        client.start()
        self.in_q.put('test')
        print(self.out_q.get())
        self.in_q.put('et tu, Brute?')
        client.join()
        
    def test_client_ping_through_io_queue(self):
        client = client_thread(self.host,
            self.port, self.in_q, self.out_q)
        #client.setDaemon(True)
        client.start()
        self.in_q.put('test')
        self.failUnless(self.out_q.get() == 'test')
        self.in_q.put('et tu, Brute?')
        client.join()
        

    






#def run_test():
#    unittest.main()

if __name__ == "__main__":

    networking_test = unittest.TestLoader().loadTestsFromTestCase(networking_udp_client_Tests)
    alltest = unittest.TestSuite([networking_test])


    result = unittest.TextTestRunner(verbosity=2).run(alltest) 
    if result.errors != []:
        sys.exit('test errors\n')
    if result.failures != []:
        sys.exit('test failures\n')
