import time
li1 = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']

def dispDig(li1):
    for i in li1:
        print(i)
        time.sleep(1)

def dispAlp(li2):
    for i in li2:
        print(i)
        time.sleep(1)

dispDig(li1)
dispAlp(li2)