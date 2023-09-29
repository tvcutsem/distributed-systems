import time
import random
from multiprocessing import Process
from ts_server   import TSServer
from ts_client   import TSClient

HOST = "localhost"
PORT = 5678

# define the processes

def server_process():
  server = TSServer(PORT)
  server.run()

def publisher_process():
  ts = TSClient(HOST, PORT)
  time.sleep(5)
  for i in range(100):
    # ('temp', sequence number, sensor id, temperature value)
    event = ('temp', i, 'sensor123', random.randint(0,50))
    print(f"publisher: emit event: '{event}'")
    ts.write(event)
    # clean up old events...
    old_event = ('temp', i-3, 'sensor123', None)
    ts.take(old_event, probe=True) # if the old_event does not exist, don't block
    time.sleep(5)

def subscriber(id):
  ts = TSClient(HOST, PORT)
  i = 0
  while True:
    if i == 0:
      # read first update
      (_, seq, _, temp) = ts.read(('temp', None, 'sensor123', None))
      i = seq
      print(f"subscriber {id}: read temperature update {seq}: {temp}")
    else:
      # read next update
      (_, seq, _, temp) = ts.read(('temp', i, 'sensor123', None))
      print(f"subscriber {id}: read temperature update {seq}: {temp}")
    i = i + 1
  
if __name__ == "__main__":
  processes = [
    Process(target=server_process),
    Process(target=publisher_process),
    Process(target=subscriber, args=("A",)),
    Process(target=subscriber, args=("B",))
  ]
  for p in processes:
    p.start()

