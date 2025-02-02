class Student:
    college = "Presidency University"
    def __init__(self, name, age, bal = 0):
        self.name = name
        self.age = age
        self.bal = bal

    def display(self):
        print(f'College: {Student.college}\nName: {self.name}\nAge: {self.age}\nBalance: {self.bal}')

s1 = Student("Madhu", 20, 1000)
s1.display()