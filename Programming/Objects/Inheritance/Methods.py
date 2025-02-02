class Student:
    def cook(self):
        print("Student can cook Maggi")
    def play(self):
        print("playing cricket")
class Employee(Student):
    def work(self):
        print("Employee can work in office")
    def cook(self):
        print("Employee can cook Pasta")
        super().cook()
        super(Student, self).cook()
e = Employee()
e.play()
    
'''
work(): Specialized Method: only in child class
play(): Inherited: used as it is in child class
cook(): Overridden Method: change implementation in child class
'''