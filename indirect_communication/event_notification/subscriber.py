import zmq
import json
from constants import *

def client():
  context = zmq.Context()
  socket = context.socket(zmq.SUB)           # create a subscriber socket
  socket.connect(f"tcp://{HOST_S}:{PORT_S}") # connect to the server
  socket.setsockopt(zmq.SUBSCRIBE, b"TEMP")  # subscribe to TEMP messages (filter on prefix)

  while True:
    msg = socket.recv()                      # receive a message related to subscription
    data = str(msg.decode()).lstrip("TEMP ") # strip the TEMP prefix
    data = json.loads(data)                  # parse the JSON object
    print(f"client: received event: {data}")     
    if (data['temp'] > 30):
      print(f"warning: high temperature measured by sensor {data['id']}")


if __name__ == "__main__":
  client()