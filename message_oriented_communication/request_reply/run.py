# helper file to start client and server in one go as subprocesses

from multiprocessing import Process
from time import sleep
from client import client
from server import server

if __name__ == "__main__":
  s = Process(target=server)
  c = Process(target=client)
  s.start()
  sleep(2)
  c.start()
  c.join()
  s.join()
