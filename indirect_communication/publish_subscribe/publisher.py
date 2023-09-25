import rabbitpy
import time
import random
import json
from constants import *

def publisher():
  connection = rabbitpy.Connection(BROKER_URL) # Connect to RabbitMQ server
  channel = connection.channel()     # Create new channel on the connection

  # Create a "topic" exchange to post sensor data
  exchange = rabbitpy.Exchange(channel, EXCHANGE_ID, exchange_type='topic')
  exchange.declare() # ensure exchange exists on the server
  # can remove using exchange.delete()

  time.sleep(5)
  for i in range(100):
    data = {'seq': i, 'id': 'sensor123', 'temp': random.randint(0,50)}
    message = rabbitpy.Message(channel, json.dumps(data)) # serialize data to string
    # Publish the message using a "routing key"
    print(f"publisher: emitting event '{data}'")
    message.publish(exchange, 'temp.sensor123')
    time.sleep(5)

if __name__ == "__main__":
	publisher()