# Python Basics

Example code demonstrating basic inter-process communication (IPC) and basic sockets API in Python.

Both IPC and sockets are examples of one-to-one "direct communication" (sender and receiver processes are coupled in time and space).

## Inter-process communication

The directory `/ipc` contains example code demonstrating basic inter-process communication (IPC) using only the standard Python library. It spawns multiple OS-level Processes, connects them via a pipe (similar to how you would connect two processes in the shell using a UNIX pipe, but bi-directional), and lets them exchange a basic message.

More information on the `multiprocessing` module can be found in the [official Python docs](https://docs.python.org/3/library/multiprocessing.html).

IPC only supports connecting processes that run within the same operating system. To connect processes that may run on different machines, we will need to use sockets.

## Sockets

The directory `/sockets` contains example code demonstrating a basic 'echo server'.
An 'echo server' is a process that listens for a message and then simply replies the same message to the sender.

In our example, the server listens on a TCP port for any message, reads the message and adds a '!' suffix (just so that we can easily tell the difference between the request and the reply message), and then sends the updated string back to the sender.

Unlike the `ipc` code, this code makes use of TCP/IP sockets instead of IPC pipes, and so one could in principle run the client and server code on different machines.

The script `run.py` programmatically launches both client and server as sub-processes of a single parent process. Alternatively and more realistically, you can open two terminals side-by-side and run `python server.py` in one terminal and `python client.py` in another.