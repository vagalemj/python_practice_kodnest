from abc import ABC, abstractmethod

class Demo1(ABC):
    @abstractmethod
    def disp1(self):
        print('Demo1 class disp1 method')

d1 = Demo1()
d1.disp1() 

'''
If abstract class doesn't have any abstract method then object for the abstract class can be created.
'''

class Demo2(ABC):
    def disp2(self):
        print('Demo2 class disp2 method')

d2 = Demo2()
d2.disp2()

'''
If abstract class have only concrete method then object for the abstract class can be created and concrete method can be called.
'''

class Demo3(ABC):
    @abstractmethod
    def disp3(self):
        print('Demo3 class disp3 method')

d3 = Demo3()
d3.disp3()

class Demo4(Demo3):
    pass

d4 = Demo4()

'''
If abstract class have only abstract method then object for the abstract class can't be created.
'''