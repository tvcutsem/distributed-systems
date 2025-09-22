from multiprocessing import Process
from constants import *
import zmq, time, pickle, random

NWORKERS = 10

def producer():
  context = zmq.Context()              
  socket  = context.socket(zmq.PUSH)      # create a push socket
  socket.bind(f"tcp://{HOST_S}:{PORT_S}") # bind socket to address
  
  while True:
    workload = random.randint(1, 30)     # compute workload
    print("Producer: created work", format(workload,'03d'))
    socket.send(pickle.dumps(workload))   # send workload to worker
    time.sleep(workload/NWORKERS)         # balance production by waiting 

def worker(id):
  context = zmq.Context()
  socket  = context.socket(zmq.PULL)         # create a pull socket
  socket.connect(f"tcp://{HOST_S}:{PORT_S}") # connect to the producer
  workerID = format(id,'03d')

  while True:
    print(f"Worker {workerID}: asking for work")
    work = pickle.loads(socket.recv())     # receive work from a source
    print(f"Worker {workerID}: got work {format(work,'03d')}")
    time.sleep(work)                       # pretend to work
    
if __name__ == "__main__":
  prod = Process(target=producer)
  workers = [Process(target=worker,args=(i+1,)) for i in range(NWORKERS)]

  for i in range(NWORKERS):
    workers[i].start()
  prod.start()

  time.sleep(30)
  for i in range(NWORKERS):
    workers[i].terminate()
  prod.terminate()

