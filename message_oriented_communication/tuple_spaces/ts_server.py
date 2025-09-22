import pickle
import zmq
from constants import *

context = zmq.Context()

# elementwise comparison using '=='
# None in the pattern matches everything
def match(tuple, pattern):
  if len(tuple) == len(pattern):
    for i in range(len(tuple)):
      if pattern[i] != None and tuple[i] != pattern[i]:
        return False
    return True
  else:
    return False

class TSServer:
  def __init__(self, port=5678):
    self.socket = context.socket(zmq.ROUTER)
    self.socket.bind(f"tcp://*:{port}")   # bind socket to address
    self.tuplespace = []                  # a Python list of Pyton tuples
    self.waitingTakers = []
    self.waitingReaders = []
    print(f"tsserver: listening on port {port}")

  def __write(self, tuple):
    # check if there are outstanding READ requests that match
    matchingReaders = [(s,patt) for (s,patt) in self.waitingReaders if match(tuple, patt)]
    # reply to the pending requests (unblocking the processes)
    for pair in matchingReaders:
        sender, _ = pair
        self.__reply(sender, [OK, tuple])
        # remove the pair from the wait list
        self.waitingReaders.remove(pair)

    # check if there are outstanding TAKE requests that match
    # only the FIRST one can fire...
    matchingTaker = next(filter(lambda pair: match(tuple, pair[1]), self.waitingTakers), None)
    if matchingTaker is not None:
      (sender, patt) = matchingTaker
      self.__reply(sender, [OK, tuple])
      self.waitingTakers.remove(matchingTaker)
    else:
      # no waiting TAKE requests match, add the tuple
      self.tuplespace.append(tuple)

  def __take(self, pattern):
    matchingTuple = next(filter(lambda tuple: match(tuple, pattern), self.tuplespace), None)
    if matchingTuple is not None:
      # remove tuple and then return it
      self.tuplespace.remove(matchingTuple)  
      return matchingTuple
    else:
      # no matching tuple found
      return None
  
  def __read(self, pattern):
    for tuple in self.tuplespace:
      if match(tuple, pattern):
        # return tuple without removing it
        return tuple
    # no matching tuples found
    return None

  def __reply(self, sender, result):
    # send a response in ZMQ's RESP format
    # frames: [receptionist id, empty frame, data frame]
    self.socket.send_multipart([
      sender,
      bytes(),
      bytes(pickle.dumps(result))])

  def run(self):
    while True:
      message = self.socket.recv_multipart()        # wait for incoming message
      # as the other peer is a REQ socket, the ROUTER receives a 3-part message:
      # [ sender identity frame, empty frame, data frame ]
      sender = message[0]
      request = pickle.loads(message[2])     # parse message into Python object
      # request = [COMMAND, tuple, probe?]
      command = request[0]

      print(f"tsserver: received command '{COMMANDS[command]}'")

      if command == WRITE:
        tuple = request[1]
        self.__write(tuple)
        self.__reply(sender, [OK])
      
      elif command == TAKE:
        pattern = request[1]
        probe = request[2]
        result = self.__take(pattern)
        if result is not None:
          self.__reply(sender, [OK, result])
        else:
          if probe:
            # just probing, respond immediately
            self.__reply(sender, [OK, None])
          else:
            # delay reply until tuple exists
            self.waitingTakers.append((sender, pattern))
      
      elif command == READ:
        pattern = request[1]
        probe = request[2]
        result = self.__read(pattern)
        if result is not None:
          self.__reply(sender, [OK, result])
        else:
          if probe:
            # just probing, respond immediately
            self.__reply(sender, [OK, None])
          else:
            # delay reply until tuple exists
            self.waitingReaders.append((sender, pattern))
      
      else:
        self.__reply(sender, [ERR, "invalid command"])


if __name__ == "__main__":
  s = TSServer()
  s.run()