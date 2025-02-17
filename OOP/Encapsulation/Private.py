class Demo1:
    def __init__(self, name):
        self.__name = name #Private variable
    def getName(self):
        return self.__name
    def setName(self, newName):
        self.__name = newName


d1 = Demo1("Madhu")
# print(d1.__name) #AttributeError: 'Demo1' object has no attribute '__name'
print(d1.getName()) #Madhu
d1.setName("Vagale") 
print(d1.getName()) #Vagale

