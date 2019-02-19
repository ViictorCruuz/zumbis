### MAIOR DE TRÊS VALORES 

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a >= b and a >= c:
    print()
    print("O maior número é o Primeiro")
elif b >= c:
    print()
    print("O maior número é o Segundo")
else:
    print()
    print("O maior número é o Terceiro")