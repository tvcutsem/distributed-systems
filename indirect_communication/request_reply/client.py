import zmq
from constants import *

def client():
  context = zmq.Context()
  socket  = context.socket(zmq.REQ)       # create request socket
  socket.connect(f"tcp://{HOST_S}:{PORT_S}") # block until connected

  socket.send(b"Hello world")             # send message
  message = socket.recv()                 # block until response
  socket.send(b"STOP")                    # tell server to stop
  print(message.decode())                 # print result


if __name__ == "__main__":
  client()