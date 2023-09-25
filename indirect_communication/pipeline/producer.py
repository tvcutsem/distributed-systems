import zmq
import time
import json
import random
import sys

from constants import *

def producer(port):
    context = zmq.Context()              
    socket  = context.socket(zmq.PUSH)      # create a push socket
    socket.bind(f"tcp://{HOST_S}:{port}")   # bind socket to address
    
    time.sleep(2)
    for i in range(10):                     # generate 10 orders
        order = json.dumps({
            'src': port,
	        'order_id': i,
            'total_value': random.randint(0,50)
	    })
        print(f"producer: submitting order: '{order}'")
        socket.send(order.encode())
        time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) > 1:
      me = str(sys.argv[1])
    else:
      me = PORT1
    producer(me)
