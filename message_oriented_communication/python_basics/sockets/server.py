from socket  import *
from constants import *

class Server:
  def run(self):
    s = socket(AF_INET, SOCK_STREAM) 
    s.bind((HOST, PORT))
    s.listen(2)
    print(f"server: accepting client connections at {HOST}:{PORT}")
    (conn, addr) = s.accept()  # returns new socket and addr. client 
    while True:                # forever
      data = conn.recv(1024)   # receive data from client
      if not data: break       # stop if client stopped
      print(f"server: received data from client: {data}")
      conn.send(data+b"!")     # return sent data plus an "!"
    print(f"server: shutting down")
    conn.close()               # close the connection

if __name__ == "__main__":
  s = Server()
  s.run()