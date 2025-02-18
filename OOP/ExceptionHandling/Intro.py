def disp(a, b):
    try:
        print(a/b) # ZeroDivisionError: division by zero
    except:
        print("Error")
    else:
        print("Else")
    finally:
        print("Finally")
disp(10, 0)
disp(10, 2)
disp(10, 5)

'''
Try: Used to keep the logic in which we may get some error.
Except: Will be executed when exception occurres in try block logic.
Else: Will be ecxecuted when try block logic executed without any error.
Finally: Will always executed irrespective of exception occurred or not.
'''