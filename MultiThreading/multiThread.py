import threading
import time
li1 = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']

def dispDig(li1):
    print(t1.is_alive())
    print(threading.current_thread)
    for i in li1:
        print(i)
        time.sleep(1)

def dispAlp(li2):
    print(threading.current_thread)
    for i in li2:
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=dispDig, args=(li1,), name="Tester")
t2 = threading.Thread(target=dispAlp, args=(li2,), name="Developer")

t1.start()
t1.join()
print(t1.is_alive())
t2.start()