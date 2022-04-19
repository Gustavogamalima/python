n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[1;33m{c} \033[0;0m', end='')
        cont += 1
    else:
        print(f'\033[1;31m{c} \033[0;0m', end='')
print(f'''
O número {n} foi divisivel {cont} vezes''')
if cont > 2:
    print('E por isso ele NÃO É PRIMO!')
else:
    print('E por isso ele É PRIMO!')
