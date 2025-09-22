from multiprocessing import Process
from publisher import publisher
from subscriber import subscriber
from time import sleep

# Make sure that a RabbitMQ server is running, or otherwise
# this program will fail (see README)

if __name__ == "__main__":
	p = Process(target=publisher)
	c1 = Process(target=subscriber, args=('1',))
	c2 = Process(target=subscriber, args=('2',))
	p.start()

	sleep(10)
	c1.start()
	c2.start()
	
	p.join()
	c1.join()
	c2.join()	
