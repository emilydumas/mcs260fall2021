"""
Thread example
"""
# MCS 260 Fall 2021 Lecture 39
import threading
import time

class BackgroundThread(threading.Thread):
    """
    Thread that does work in the background
    """
    def run(self):
        "Main work of the thread"
        for i in range(10):
            print("Background Thread {}".format(i),flush=True)
            time.sleep(1)


T = BackgroundThread(daemon=True)
T.start()  # starts the new thread, calling T.run() in that thread

for i in range(15):
    print("Main Thread {}".format(i),flush=True)
    time.sleep(0.3)
