'''
Public: It should be accessed inside the class, outside the class, and by the child class.
Protected: It should be accessed inside the same class in which we have declared it and inside child class.
Private: It should be accessed only inside the same class in which we have declared it.
Access Modifiers/Specifiers: Public, Protected, Private is used to determine the accessibility of a data member and member function.
'''

class Demo1:
    def __init__(self, name):
        self.fname = name
    def display(self):
        print(self.fname)
    
d1 = Demo1("Madhu")
print(d1.fname)
d1.display()

class Demo2(Demo1):
    def display1(self):
        print(self.fname)

d2 = Demo2("Vagale")
print(d2.fname)
d2.display()


print('==========================================')


'''
The variables which are public can be accessed inside 
the same class, outside of any class, and inside the child class 
and inside non-child class.
'''