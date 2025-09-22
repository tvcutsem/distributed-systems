import rabbitpy
import sys
import json
import os

from constants import *
from time import sleep

def consumer(id):
  connection = rabbitpy.Connection(BROKER_URL)
  channel = connection.channel()

  queue = rabbitpy.Queue(channel, QUEUE_NAME)
  queue.declare() # ensure queue exists on the server

  print(f"consumer {id}: connected to queue")

  # while there are messages in the queue, fetch them (using AMQP Basic.Get)
  while len(queue) > 0:
    message = queue.get()
    data = json.loads(message.body.decode())
    print(f"consumer {id}: received order {data}")
    # explicitly acknowledge message receipt after successful processing
    message.ack()
    sleep(1)

if __name__ == "__main__":
  if len(sys.argv) > 1:
     me = sys.argv[1]
  else:
     me = os.getpid()
  consumer(me)