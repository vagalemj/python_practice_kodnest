class Demo:
    def disp(self):
        print('Inside disp with 0 arguments')
    def disp(self, a):
        print('Inside disp with 1 argument')
    def disp(self, a, b):
        print('Inside disp with 2 arguments')

d = Demo()
#d.disp()
#d.disp(10)
d.disp(10, 20)

# Python doesn't support method overloading. The last method definition will be considered.