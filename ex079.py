numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! não adicionar...')
    desejo = ' '
    while True:
        desejo = str(input('Quer continuar? [S/N]')).strip().lower()[0]
        break
    if desejo == 'n':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
