# Dunder method: The dunder methods which has suffix and prefix as __ these methods can be called
# as magic methods because as programmer we no need to call any methods, automatically methods
# will be called.

class Demo1:
    def __str__(self, other):
        self.a = 10
        other.b = 20
        return self.a - other.b

class Demo2:
    def __str__(self):
        return 'Hi'
   

d1 = Demo1()
d2 = Demo2()
print(d1)
print(d2)
print(d1-d2) 

'''
In Python if we print reference variable then initially python will invoke __str__ method.
which will always returns string representation of an address of an object().

In the above example we have overridden __str__ method in their respective classes.
'''