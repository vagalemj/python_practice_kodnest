class Bank:
    bank_name = 'HDFC'
    def __init__(self, name, age, bal):
        self.user_name = name
        self.age = age
        self.user_balance = bal
    
    def display_user(self):
        print(f'User name: {self.user_name} \nUser age: {self.age} \nUser balance: {self.user_balance} \nBank name: {self.bank_name}')

c1 = Bank('Madhu', 25, 1000)
c1.display_user()
