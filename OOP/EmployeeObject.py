class Employee:
    company = "Google"
    def __init__(self, name, age, desi):
        self.emp_name = name
        self.emp_age = age
        self.emp_designation = desi

    def login(self, time):
        print(f'Employee {self.emp_name} has logged in at {time}')
    
    def logout(self, time):
        print(f'Employee {self.emp_name} has logged out at {time}')

    def work(self, hours):
        print(f'Employee {self.emp_name} is working on {hours}')

    def display_emp(self):
        print(f'Employee name: {self.emp_name} \nEmployee age: {self.emp_age} \nEmployee designation: {self.emp_designation} \nCompany name: {self.company}')

e1 = Employee('Madhu', 25, 'Software Engineer')
e2 = Employee('Raj', 30, 'Manager')
e1.display_emp()
e2.display_emp()
e1.login('9:00 AM')
e1.work('Python')
e1.logout('6:00 PM')
e2.login('9:00 AM')
e2.work('Meeting')
e2.logout('6:00 PM')
