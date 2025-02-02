class Demo:
    def disp(self):
        print('Inside disp method of Demo class')

class NewDemo(Demo):
    pass

d1 = NewDemo()
d1.disp() # Inside disp method of Demo class