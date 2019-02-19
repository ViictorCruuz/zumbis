### CALCULE A SOMA DE NÚMEROS INTEIROS ATÉ SER DIGITADO ZERO

soma = 0
while True:
    x = int(input("Digite um número ou (pressione 0) para sair : "))
    if x == 0:
        break
    soma = soma + x
print("Soma: %d" %soma)