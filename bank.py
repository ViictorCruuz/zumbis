class Client:
    def __init__(self, name, telephone, password):
        self.name = name
        self.telephone = telephone
        self.password = password

class Account:
    def __init__(self, clients, agency_number, account_number, digit, balance='10,2B'):
        self.clients = clients
        self.agency_number = agency_number
        self.account_number = account_number
        self.digit = digit
        self.balance = balance

    def summary(self):
        print('CC Number: ', self.account_number, 'CC Agency: ', self.agency_number)
        print('Digit: ', self.digit, '\n', 'Balance: ', self.balance)

    def sake(self, value):
        if self.balance >= value:
            self.balance -= value

    def deposit(self, value):
        self.balance += value