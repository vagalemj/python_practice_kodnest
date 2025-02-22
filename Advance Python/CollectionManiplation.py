li = [1, 2, 3, 4, 5]

def double(num):
    return num * 2

double_li = list(map(double, li))
print(double_li)

def checkEven(num):
    return num % 2 == 0

even_li = list(filter(checkEven, li))
print(even_li)


from functools import reduce
def mul(a, b):
    return a * b

res = reduce(mul, li)
print('Multiplication is: ', res)