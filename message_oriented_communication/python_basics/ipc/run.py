from multiprocessing import Process, Pipe
import os

def server(conn):
	print(f"Hello from server process {os.getpid()}")
	data = conn.recv()
	print(f"server received data: {data}")
	conn.close()

def client(conn):
	print(f"Hello from client process {os.getpid()}")
	values = [42, "hello world", {"key": "value"}]
	conn.send(values)
	print(f"client sent data {values}")
	conn.close()

if __name__ == "__main__":
    # construct a pipe to connect two processes
	(p1_conn, p2_conn) = Pipe()
	p1 = Process(target=server, args=(p1_conn,))
	p2 = Process(target=client, args=(p2_conn,))
	# run both processes in parallel
	p1.start()
	p2.start()
	# wait for both processes to finish
	p1.join()
	p2.join()

  

  
