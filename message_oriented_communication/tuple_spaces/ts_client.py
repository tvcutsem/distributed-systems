import pickle
import zmq
from constants import *
context = zmq.Context()

class TSClient:
  def __init__(self, host, port):
    self.socket = context.socket(zmq.REQ)        # create request socket
    self.socket.connect(f"tcp://{host}:{port}")  # block until connected

  def __sendrecv(self, message):            # this is a private method
    self.socket.send(pickle.dumps(message)) # serialize and send
    message = self.socket.recv()            # block until response
    return pickle.loads(message)            # deserialize response

  def write(self, tuple):
    """write a tuple. Never blocks."""
    reply = self.__sendrecv([WRITE, tuple])
    if reply[0] == OK:                      # check status code
      return None
    else: # reply[0] == ERR
      raise ValueError(reply[1])
  
  def take(self, pattern, probe=False):
    """remove matching tuple, blocking if none match and probe is False"""
    status, reply = self.__sendrecv([TAKE, pattern, probe])
    if status == OK:
      return reply
    else: # status == ERR
      raise ValueError(reply)
    
  def read(self, pattern, probe=False):
    """read matching tuple, blocking if none match and probe is False"""
    status, reply = self.__sendrecv([READ, pattern, probe])
    if status == OK:
      return reply
    else: # status == ERR
      raise ValueError(reply)
