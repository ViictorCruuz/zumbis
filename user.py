from bank import Client, Account

john = Client('John Smith', '142-4134-31', '****')
beth = Client('Beth Keen', '930-8812-65', '****')

print(('Name: %s \nCell phone: %s \nPassword: %s') %
        (john.name, john.telephone, john.password))

print((' '))