def disp(a, b):
    try:
        print(a/b) # ZeroDivisionError: division by zero
    except:
        print("Error")
disp(10, 0)
disp(10, 2)
disp(10, 5)