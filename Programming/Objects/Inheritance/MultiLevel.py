class Demo1():
    def disp1(self):
        print('Inside disp1 method of Demo1 class')
class Demo2(Demo1):
    def disp2(self):
        print('Inside disp2 method of Demo2 class')
class Demo3(Demo2):
    pass

d3 = Demo3()
d3.disp1()
d3.disp2()