def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Error")
    except NameError:
        print("NameError")
    except TypeError:
        print("TypeError")

disp(10, 'Madhu')