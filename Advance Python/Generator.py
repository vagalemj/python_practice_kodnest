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