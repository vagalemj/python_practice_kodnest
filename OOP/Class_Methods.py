class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self):
        print(f'{self.name} is working')

e1 = Employee('Madhu', 25)
e1.work()