from multiprocessing import Process
from producer import producer
from consumer import consumer
from time import sleep

# Make sure that a RabbitMQ server is running, or otherwise
# this program will fail (see README)

if __name__ == "__main__":
	p = Process(target=producer)
	c = Process(target=consumer, args=('1',))
	p.start()

	sleep(6)
	c.start()
	
	p.join()
	c.join()
	
