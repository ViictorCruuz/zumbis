
# class Television:
#     def __init__(self):  # função construtora
#         """ Funções que tem double under, são funções reservadas do Python
#         você não costuma chamá-la diretamente, são chamadas debaixo do pano """
#     self.switched = True
#     self.channel = 5


class Client:
    def __init__(self, name, telephone, password):
        self.name = name
        self.telephone = telephone
        self.password = password

class Account:
    def __init__(self, clients, account_number, account_agency, digit, balance = '$ 2,5K'):
        self.balance = balance
        self.clients = clients
        self.account_number = account_number
        self.account_agency = account_agency
        self.digit = digit
        
    def summary(self):
        print('CC Number: ', self.account_number, '\n', 'CC agency:', self.account_agency)
        print('Digit: ', self.digit, '\n', 'Balance: ', self.balance)
    def sake(self, value):
        if self.balance >= value:
            self.balance -= value
    def deposit(self, value):
        self.balance += value
