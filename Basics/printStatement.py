# Scripting way to write a code in python
print("Scripting way of Hello, World!")


# Function(Procedural) way to write a code in python
def message():
    print("Procedural way of Hello, World!")
message()
# Indentation: Python uses indentation to define block-level structure. 
# An indentation is a space or a group of spaces at the beginning of a line that defines the block of code.


# Object Oriented way to write a code in python
class Message:
    def instance_method(self):
        print("Object oriented way of Hello, World!")
d1 = Message()
d1.instance_method()


# Using end parameter in print function
print("Hello,", end=" ")
print("World!")


# Using \t in print function
print("Hello\tWorld")


# Using \n in print function
print("Hello\nWorld")


#Example
class demo:
    def disp(self):
        print('Start')
        print('Hello')
        print('World')
        print('End')
    def disp1(self):
        d2 = demo()
        d2.disp()
d1 = demo()
d1.disp1()