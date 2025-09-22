import rabbitpy
import time
import random
import json
from constants import *

def producer():
  connection = rabbitpy.Connection(BROKER_URL) # Connect to RabbitMQ server
  channel = connection.channel()     # Create new channel on the connection

  queue = rabbitpy.Queue(channel, QUEUE_NAME) # Create a work queue
  queue.declare() # make sure it exists on the server

  time.sleep(5)
  for i in range(100):
    data = {'order_id': i, 'total_value': random.randint(0,50)}
    message = rabbitpy.Message(channel, json.dumps(data)) # serialize data to string
    # Publish the message directly to the queue
    message.publish('', QUEUE_NAME)
    print(f"producer: submitted order '{data}'")
    time.sleep(5)

if __name__ == "__main__":
	producer()