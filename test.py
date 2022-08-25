import time
import threading

from sick import removal_statistic

StartTime = time.time()
stopEvent = None

def __setInterval(interval, action, stopEvent):
    nextTime = time.time()+interval
    while not stopEvent.wait(nextTime-time.time()):
        nextTime += interval
        action()

def cancel():
    stopEvent.set()

def start_thread(player, add_info):
    global stopEvent
    stopEvent = threading.Event()
    thread = threading.Thread(target=__setInterval, args=[
                            10, lambda:removal_statistic(player,add_info), stopEvent])
    thread.start()
    
    t = threading.Timer(100, cancel)
    t.start()
    
