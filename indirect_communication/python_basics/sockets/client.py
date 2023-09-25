from socket  import *
from constants import *

class Client:
  def run(self):
    s = socket(AF_INET, SOCK_STREAM)
    print(f"client: connecting to server at {HOST}:{PORT}")
    s.connect((HOST, PORT)) # connect to server (block until accepted)
    s.send(b"Hello, world") # send same data
    data = s.recv(1024)     # receive the response
    # print what you received
    print(f"client: received data from server: {data}")
    s.send(b"")             # tell the server to close
    s.close()               # close the connection

if __name__ == "__main__":
  c = Client()
  c.run()