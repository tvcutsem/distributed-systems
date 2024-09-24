import zmq
import sys
from constants import *

def client():
  message = sys.argv[1] if len(sys.argv) > 1 else ""

  context = zmq.Context()
  socket  = context.socket(zmq.REQ)       # create request socket
  socket.connect(f"tcp://{HOST_S}:{PORT_S}") # block until connected

  socket.send(message.encode())           # send message
  response = socket.recv()                # block until response
  #socket.send(b"STOP")                   # tell server to stop
  print(response.decode())                # print result


if __name__ == "__main__":
  client()