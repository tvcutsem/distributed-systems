import zmq
import json
import sys
import os

from constants import *

def consumer(pid):
  context = zmq.Context()
  s = context.socket(zmq.PULL)       # create a pull socket
  s.connect(f"tcp://{SRC1}:{PORT1}") # connect to task source 1
  # s.connect(f"tcp://{SRC2}:{PORT2}") # connect to task source 2

  while True:
    print(f"consumer {pid}: waiting for orders")
    order = json.loads(s.recv().decode())  # receive msg from any task source
    print(f"consumer {pid}: received order {order}")

if __name__ == "__main__":
  pid = os.getpid()
  consumer(pid)