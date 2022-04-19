print('='*50)
print('''      10 TERMOS DE UMA PA       ''')
print('='*50)
pt = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = pt + (10 - 1) * razao
for c in range(pt, decimo + razao, razao):
    print(f'{c} -> ', end='')
print('ACABOU')
