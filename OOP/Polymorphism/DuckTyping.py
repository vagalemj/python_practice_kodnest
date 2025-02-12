

class add:
    def calculate(self, a, b):
        print('Addition: ', a+b)

class sub:
    def calculate(self, a, b):
        print('Subtraction: ', a-b)

class mul:
    pass

def op(ref, a, b):
    if type(ref).__name__ == 'mul':
        print('Multiplication: ', a*b)
    else:
        ref.calculate(a, b)

op(add(), 10, 40)
op(sub(), 40, 10)
op(mul(), 10, 20)