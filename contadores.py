
###  USANDO 'IF' PARA PRINTAR APENAS OS VALORES PARES
n = int(input("Escreve um número: "))
x = 0
while x <= n:
    if x %2 == 0:
        print(x)
    x += 1

### SEM USAR O 'IF' PARA PRINTAR APENAS OS VALORES PARES
z = int(input("Escreve um número: "))
y = 0
while y <= n:
    print(y)
    y += 2

### USANDO 'FOR' PARA PRINTAR APENAS OS VALORES PARES
a = range(11)
print('Iniciando agora a partir da variável "a"')
for b in a:
    if b %2 == 0:
        print(b)

############ NÚMEROS ÍMPARES ###############

n = int(input("Escreve um número: "))
x = 1
while x <= n:
    if x %2 != 0:
        print(x)
    x += 1

