from banco import Cliente, Conta, ContaEspecial

joão = Cliente('João da Silva', '777-1234')
maria = Cliente('Maria da Silva', '333-9876')

conta1 = Conta([joão], 1, 1000)
conta2 = ContaEspecial([maria, joão], 2, 500, 1000)

print( ('Name: %s \n Cell phone: %s')
        % (joão.nome, joão.telefone))

conta1.saque(50)
conta1.saque(190)
conta1.extrato()

print( ('Nome: %s \n Nome: %s')
        % (maria.nome, joão.nome))

conta2.deposito(300)
conta2.deposito(95.15)
conta2.saque(895.16)
conta2.extrato()

