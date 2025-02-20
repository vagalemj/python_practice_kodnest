import threading
import time

def process_request(user):
    print(f'Processing request from {user}')
    time.sleep(3)
    print(f'Finished processing request from {user}')

t1 = threading.Thread(target=process_request, args=('user1',))
t2 = threading.Thread(target=process_request, args=('user2',))
t3 = threading.Thread(target=process_request, args=('user3',))

t1.start()
t2.start()
t3.start()