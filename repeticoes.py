# print(1)'
# print(2)
# print(3)

# print()

# x = 1
# while x <= 5:
#     print(x)
#     x += 1'


n = int(input('Usário, digite um número: '))

x = 1
while x <= n:
    print(x)
    x += 1


def test(foundN):
    if foundN %2 == 0:
        print('The number is {}'.format(foundN), 'is ok!')
    else:
        print('Try again with other number.')

test(15)