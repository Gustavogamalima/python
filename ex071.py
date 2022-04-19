c200 = c100 = c50 = c20 = c10 = c5 = c1 = 0
print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)
valor = float(input('Que valor você quer sacar? R$'))
if valor > 200:
    while valor >= 200:
        valor = valor - 200
        c200 += 1
    print(f'Total de {c200} cédulas de R$200')
if valor > 100:
    while valor >= 100:
        valor = valor - 100
        c100 += 1
    print(f'Total de {c100} cédulas de R$100')
if valor > 50:
    while valor >= 50:
        valor = valor - 50
        c50 += 1
    print(f'Total de {c50} cédulas de R$50')
if valor > 20:
    while valor >= 20:
        valor = valor - 20
        c20 += 1
    print(f'Total de {c20} cédulas de R$20')
if valor > 10:
    while valor >= 10:
        valor = valor - 10
        c10 += 1
    print(f'Total de {c10} cédulas de R$10')
if valor > 5:
    while valor >= 5:
        valor = valor - 5
        c5 += 1
    print(f'Total de {c5} cédulas de R$5')
if valor > 1:
    while valor >= 1:
        valor = valor - 1
        c1 += 1
    print(f'Total de {c1} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
