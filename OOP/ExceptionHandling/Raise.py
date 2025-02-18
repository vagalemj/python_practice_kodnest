# def disp(a, b):
#     print(a/c)
# disp(10, 0) # ZeroDivisionError: division by zero

# def disp(a, b):
#     print(a/c)
# disp(10, 2) # NameError: name 'c' is not defined

# def disp(a, b):
#     print(a/b)
# disp(10, 'Madhu') # TypeError: unsupported operand type(s) for /: 'int' and 'str' 

def checkAge(age):
    if(age < 18):
        raise ValueError("Age is less than 18")

try:
    checkAge(17)
except ValueError as e:
    print(e)