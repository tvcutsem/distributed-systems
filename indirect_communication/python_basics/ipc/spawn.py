from multiprocessing import Process
import os

def info():
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def hello(name):
    print('hello ', name)
    info()

if __name__ == '__main__':
    info()
    p = Process(target=hello, args=('world',))
    p.start()
    p.join()