"""
Producer-consumer example (multiple consumers)
"""
# MCS 260 Fall 2021 Lecture 39 (add-on example posted after lecture)
import threading
import time
import random
import queue

class WorkerThread(threading.Thread):
    """
    Thread that does work in the background, taking jobs from
    a specified queue.Queue
    """
    def __init__(self,Q,workernumber=0):
        """
        Make a new worker that receives its work from
        a queue.Queue object Q
        """
        super().__init__()
        self.workernumber = workernumber
        self.Q = Q  # save Q so we can access it in .run()
        self.idstr = "Worker {}".format(self.workernumber)

    def run(self):
        "Main work of the thread"
        while True:
            x = self.Q.get()
            if x == None:
                print(self.idstr,"shutting down on request")
                break
            print(self.idstr,"now working on {}".format(x),flush=True)
            time.sleep(2*random.random())
            print(self.idstr,"finished job {}".format(x),flush=True)

jobqueue = queue.Queue()

num_workers = 10
num_jobs = 30

print("Starting {} worker threads".format(num_workers))
workers = [ WorkerThread(jobqueue,i) for i in range(num_workers) ]
for T in workers:
    T.start()

for i in range(num_jobs):
    print("Submit job {}".format(i),flush=True)
    jobqueue.put(i)
    if random.random() < 0.25:
        # 25 % chance we pause
        time.sleep(0.5 + 2.5*random.random())

print("Adding None(s) to the queue so the worker quits when done")

# We need to add `num_workers` copies of None to the queue so that
# each thread gets one.  (Could handle this in other ways, e.g. by
# setting an attribute of each thread that signals completion.)
for _ in range(num_workers):
    jobqueue.put(None)
