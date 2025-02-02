class Demo1():
    def disp1(self):
        print('Inside disp1 method of Demo1 class')
class Demo2(Demo1):
    def disp2(self):
        print('Inside disp2 method of Demo2 class')
class Demo3(Demo1):
    pass

d1 = Demo2()
d1.disp1()
d1.disp2()
d2 = Demo3()
d2.disp1()