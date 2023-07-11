import time
from threading import Thread

def do_this():
    print('Starting this!')
    time.sleep(2)
    print("Did this!")

def do_that():
    print("Starting that!")
    time.sleep(3)
    print("Did that!")


t1 = Thread(target=do_this)
t1.start()

t2 = Thread(target=do_that)
t2.start()

# threads split the proces memory in two processes that runs together. 
# It makes your program faster