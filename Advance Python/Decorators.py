def decor(func):
    def inner(name):
        if name == "Madhu":
            print(name, 'is learning Python')
        else:
            func(name)
    return inner
@decor
def choice(name):
    print(name, 'is learning Java')

choice('Madhu')
choice('Sudhan')


def smartdiv(func):
    def inner(a, b):
        if b == 0:
            print('b should not be 0')
        else:
            func(a,b)
    return inner

@smartdiv
def div(a, b):
    print('Division is: ', a/b)

div(12, 2)
div(10,0)



def repeat(num):
    def outer(func):
        def inner():
            for i in range(num):
                func()
        return inner
    return outer

@repeat(num = 4)
def msg():
    print('Hello')
msg()