import threading
import time

def background_task():
    while True:
        print('Background task is running....')
        time.sleep(1)

thread = threading.Thread(target=background_task)
thread.daemon = True
thread.start()

time.sleep(3)
print('Main program ends...')