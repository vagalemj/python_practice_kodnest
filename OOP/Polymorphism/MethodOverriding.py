# In this code we are achieving polymorphism using method overriding.

class Calculator:
    def calculate(self, a, b):
        pass

class add(Calculator):
    def calculate(self, a, b):
        print('Addition: ', a+b)

class sub(Calculator):
    def calculate(self, a, b):
        print('Subtraction: ', a-b)

class mul(Calculator):
    pass


ref = add()
ref.calculate(10, 40)

ref = sub()
ref.calculate(40, 10)

ref = mul()
ref.calculate(10, 20)

def op(ref, a, b):
    ref.calculate(a, b)

op(add(), 10, 40)
op(sub(), 40, 10)
op(mul(), 10, 20)