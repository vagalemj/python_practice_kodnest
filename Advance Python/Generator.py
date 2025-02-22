# def disp():
#     return 10
#     return 20
#     return 30

# print(disp())

def gene():
    yield 10
    yield 20
    yield 30

test = gene()
print(next(test))
print(next(test))
print(next(test))

def fibo(num):
    a, b = 0, 1
    for i in range(num):
        print(a)
        a,b = b, a+b

fibo(10)


def fibo_gen(num):
    a, b = 0, 1
    for i in range(num):
        yield a
        a,b = b, a+b

ref = fibo_gen(10)
print(next(ref))
print(next(ref))

# for i in ref(5):
#     print(next(ref))