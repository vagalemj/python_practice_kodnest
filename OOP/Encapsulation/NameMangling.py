class Demo1:
    def __init__(self, name):
        self.__name = name #Private variable
    
d1 = Demo1("Madhu")
# print(d1.__name) #AttributeError: 'Demo1' object has no attribute '__name'
print(d1._Demo1__name) #Madhu

'''
1. NameMangling is a process of providing new name to the private variable.

2. These new names will be provided automatically by python for all private members.

3. New Name will be provided in the format: objectName._className__variableName
'''