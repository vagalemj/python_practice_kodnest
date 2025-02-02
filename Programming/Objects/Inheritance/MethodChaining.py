'''
Method Chaining: is a process of calling one method from another method.
'''

class Grandparent:
    def cook(self):
        print("Grandparent can cook Biriyani")

class Parent(Grandparent):
    def cook(self):
        print("Parent can cook Chicken")

class Child(Parent):
    def cook(self):
        print("Child can cook Egg")
        super().cook()
        super(Parent, self).cook()

c = Child()
c.cook()