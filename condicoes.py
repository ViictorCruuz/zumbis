a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    print('Número {} é maior do que {}'.format(a,b))

elif a < b:
    print('Número {} é menor do que {}'.format(a,b))
elif a == b:
    print('Os números digitados são iguais!')