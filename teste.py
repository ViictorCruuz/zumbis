from classes import Client, Account

victor = Client('Victor dos Santos Cruz', '11 91234-5678', '****')
marcela = Client('Marcela Santos Azevedo', '11 99876-5432', '****')
print()
print('$$$$$$   >>>  VICTOR <<<   $$$$$$')
print()
print( ('Name: %s \n Cell phone: %s')
        % (victor.name, victor.telephone))
account1 = Account([victor], '1010', 11111, 1)
account1.summary()
print()
print('$$$$$$   >>>  MARCELA <<<   $$$$$$')
print()
print( ('Name: %s \n Cell phone: %s.')
        % (marcela.name, marcela.telephone))
account2 = Account([marcela], '2020', 22222, 2)
account2.summary()
print()

