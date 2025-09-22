from multiprocessing import Process
from ts_server   import TSServer
from ts_client   import TSClient

HOST = "localhost"
PORT = 5678

# helper functions

def factorial(n):
  res = 1
  while n > 0:
    res = res * n
    n = n - 1
  return res

def fibonacci(n):
    if n in {0, 1}:
        return n
    prev, next = 0, 1
    for _ in range(2, n + 1):
        prev, next = next, prev + next
    return next

# define the processes

def server_process():
  server = TSServer(PORT)
  server.run()

def master_process():
  ts = TSClient(HOST, PORT)
  ts.write(("fac", 5))
  ts.write(("fib", 3))
  fac_res, fac = ts.take(("fac_res", None))
  print(f"master: got fac result: {fac}")
  fib_res, fib = ts.take(("fib_res", None))
  print(f"master: got fib result: {fib}")

def fac_worker():
  ts = TSClient(HOST, PORT)
  fac, n = ts.take(("fac", None))
  print(f"fac_worker: got work: fac({n})")
  result = factorial(n)
  ts.write(("fac_res", result))

def fib_worker():
  ts = TSClient(HOST, PORT)
  fac, n = ts.take(("fib", None))
  print(f"fib_worker: got work: fib({n})")
  result = fibonacci(n)
  ts.write(("fib_res", result))
  
if __name__ == "__main__":
  processes = [
    Process(target=server_process),
    Process(target=master_process),
    Process(target=fac_worker),
    Process(target=fib_worker)
  ]
  for p in processes:
    p.start()

