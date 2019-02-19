# n = 1
# soma = 0
# while n <= 10:
#     x = int(input("digite o %dº número: " %n))
#     soma = soma + x
#     n += 1
# print("Soma: %d" %soma)


# ### MÉDIA DE 10 VALORES
# a = 1
# total = 0
# while a <= 10:
#     b = int(input("Digite o %dº número: " %a))
#     total = total + b
#     c = total / 10
#     a += 1
# print("Soma de todos os valores digitados: %d" %total)
# print("Média de todos esses valores: %2.1f" %c)
#
# ### MESMO PROBLEMA OUTRA RESOLUÇÃO
# n = 1
# soma = 0
# while n <= 10:
#     x = int(input("Digite o %dº número:" %n))
#     soma = soma + x
#     n = n + 1
# print("Média: %5.2f" %(soma/10))

### CALCULE O FATORIAL DE 10
cont = 1
fat = 1
n = int(input("Digite n: "))
while cont <= n:
    fat = fat * cont
    cont += 1
print("O fatorial de %d é: %d " % (n, fat))


