import multiprocessing
from server import *
from client import *

def server():
	s = Server()
	s.run()

def client():
	c = Client()
	c.run()

if __name__ == "__main__":
	s = multiprocessing.Process(target=server)
	c = multiprocessing.Process(target=client)

	s.start()
	c.start()
	s.join()
	c.join()

  

  
