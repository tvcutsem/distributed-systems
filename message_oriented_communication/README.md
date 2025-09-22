# Lecture on Message-oriented Communication

This directory contains the code examples from the lecture on Message-oriented Communcation.

The examples demonstrate various patterns of inter-process communication using Python and two modern middleware libraries: ZeroMQ and RabbitMQ.

See below for installation instructions.

## Communication Patterns

The repository covers the communication patterns discussed during the lecture:

  1. [Request-reply](./request_reply)
  2. [Event notification](./event_notification)
  3. [Pipeline](./pipeline)
  4. [Publish-subscribe](./publish_subscribe)
  5. [Message queuing](./message_queue)
  5. [Tuple spaces](./tuple_spaces)

Check the `README.md` in each subdirectory for details.

If you are unfamiliar with processes or remote communication in Python, have a look at the code examples in `python_basics`.

## Installation

Make sure you have a recent [Python3](https://www.python.org/downloads/) installed.

  * Create a virtual environment, e.g. `python3 -m venv distsys_venv`
  * Activate it: `source distsys_venv/bin/activate`
  * Install library dependencies: `pip install -r requirements.txt`

The patterns [Request-reply](./request_reply), [Event notification](./event_notification) and [Pipeline](./pipeline) are examples of "direct communication" and use a library called [ZeroMQ](https://zeromq.org/).

The patterns [Publish-subscribe](./publish_subscribe) and [Message queuing](./message_queue) are examples of "indirect communication" and use a system called [RabbitMQ](https://www.rabbitmq.com/).

See below for more information about these libraries.

## Middleware used

### ZeroMQ

[ZeroMQ](https://zeromq.org/) describes itself as "An open-source universal messaging library".

ZeroMQ is a C library (with wrapper libraries for many other languages including Python) that was designed for message-oriented communication between processes in the style of the Berkeley sockets API, but with much more flexibility in terms of how processes can connect, how messages are routed between sockets, and with a higher-level API (discrete messages instead of bytestreams).

Our examples use the [zmq](https://pyzmq.readthedocs.io/en/latest/) Python bindings for ZeroMQ.

### RabbitMQ

[RabbitMQ](https://www.rabbitmq.com/) describes itself as "the most widely deployed open source message broker".

Installation instructions can be found [here](https://www.rabbitmq.com/install-homebrew.html).

RabbitMQ is a message broker that runs as a separate process on your machine. Some of the examples depend on a rabbitmq server running on your local machine.

By default the rabbitmq server will listen on port 5672. A web-based management interface is available via [http://localhost:15672](http://localhost:15672) (default username/password: `guest/guest`). This allows you to inspect, in real-time, all queues, exchanges, messages and connections created by client programs.

We use the [rabbitpy](https://rabbitpy.readthedocs.io/en/latest/index.html) Python client library to interact with the RabbitMQ server from Python code.

## Acknowledgements

The inspiration for these code examples comes from the [Distributed Systems](https://www.distributed-systems.net/index.php/books/ds4/) 4th edition book of Maarten van Steen and Andrew Tanenbaum. You can download a free copy of the book for educational purposes from their website.

Some of the code in this repository is based on example code from the ZeroMQ and RabbitMQ documentation.

The tuple space API and some of the example code in `tuple_spaces/` was inspired by [dRuby](https://www.druby.org/sidruby/the-druby-book.html) and its [Rinda](https://www.druby.org/sidruby/6-coordinating-processes-using-rinda.html) tuple spaces.
