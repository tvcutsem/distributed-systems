import zmq
import json
import sys

from constants import *

def worker(me):
  context = zmq.Context()
  s = context.socket(zmq.PULL)       # create a pull socket
  s.connect(f"tcp://{SRC1}:{PORT1}") # connect to task source 1
  # s.connect(f"tcp://{SRC2}:{PORT2}") # connect to task source 2
  print(f"worker {me}: waiting for orders")

  while True:
    order = json.loads(s.recv().decode())  # receive msg from any task source
    print(f"consumer {me}: received order {order}")

me = str(sys.argv[1])
worker(me)