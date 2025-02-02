'''
class Demo1:
    def disp(self):
        print("Demo1 disp1")
class Demo2:
    def disp(self):
        print("Demo2 disp2")
class Demo3(Demo1, Demo2):
    pass

d = Demo3()
d.disp()
'''

class Demo1:
    def __init__(self):
        self.x = 100
class Demo2:
    def __init__(self):
        self.x = 200
class Demo3(Demo2, Demo1):
    def __init__(self):
        self.x = 300

d3 = Demo3()
print(d3.x)

# MRO - Method Resolution Order: It is the order in which the methods are resolved in the multiple inheritance scenario.