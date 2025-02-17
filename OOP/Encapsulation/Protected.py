class Demo1:
    def __init__(self, name):
        self._fname = name #Procted variable
    def display(self):
        print(self._fname)
    
d1 = Demo1("Madhu")
print(d1._fname)
d1.display()

class Demo2(Demo1):
    def display1(self):
        print(self._fname)

d2 = Demo2("Vagale")
print(d2._fname)
d2.display()

class Demo3:
    def display2(self):
        print(d1._fname)
d3 = Demo3()
d3.display2()

print('==========================================')


'''
The variables which are protected can be accessed inside same class, outside of any class, and inside the child class inside non-child class.

The variable which are protected should be accessed inside same class and inside the child class and this is programmers duty to follow there rules.
'''