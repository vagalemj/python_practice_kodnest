class MathOperation:
    @staticmethod
    def add(a, b):
        return a + b
    def calc(self):
        pass

res = MathOperation.add(10, 20)
print(res)

math_op = MathOperation()
print(math_op.add(30, 20)) # AttributeError: 'MathOperation' object has no attribute 'add'