import rabbitpy
import sys
import json
from constants import *
import os

def subscriber(id):
  with rabbitpy.Connection(BROKER_URL) as conn:
      with conn.channel() as channel:
          queue = rabbitpy.Queue(channel, f'subscriber-{id}')
          queue.declare() # ensure queue exists on the server
          queue.bind(EXCHANGE_ID, 'temp.*') # Bind queue to exchange via routing key

          print(f"subscriber {id}: connected to queue")

          try:
              # Consume messages in queue (blocking if none are available)
              for message in queue:
                data = json.loads(message.body.decode())
                print(f"subscriber {id}: got message {data}")
                if (data['temp'] > 30):
                    print(f"warning: high temperature measured by sensor {data['id']}")
                # explicitly acknowledge message receipt after successful processing
                message.ack()

          # Exit on CTRL-C
          except KeyboardInterrupt:
              print(f'subscriber {id}: stopped')


if __name__ == "__main__":
  if len(sys.argv) > 1:
     me = sys.argv[1]
  else:
     me = os.getpid()
  subscriber(me)