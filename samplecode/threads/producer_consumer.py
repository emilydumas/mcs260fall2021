"""
Producer-consumer example (with one consumer)
"""
# MCS 260 Fall 2021 Lecture 39
import threading
import time
import random
import queue

class WorkerThread(threading.Thread):
    """
    Thread that does work in the background
    """
    def __init__(self,Q):
        """
        Make a new worker that receives its work from
        a queue.Queue object Q
        """
        super().__init__()
        self.Q = Q  # save Q so we can access it in .run()
    
    def run(self):
        "Main work of the thread"
        while True:
            x = self.Q.get()
            if x == None:
                print("Worker Thread shutting down on request")
                break
            print("Worker Thread now working on {}".format(x),flush=True)
            time.sleep(2*random.random())

jobqueue = queue.Queue()

T = WorkerThread(jobqueue)
T.start()  # starts the new thread, calling T.run() in that thread

for i in range(30):
    print("Submit job {}".format(i),flush=True)
    jobqueue.put(i)

print("Adding None to the queue so the worker quits when done")
jobqueue.put(None)
