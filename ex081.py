numbers = []
while True:
    numbers.append(int(input('Digite um valor: ')))
    desire = ' '
    while True:
        desire = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        break
    if desire == 'n':
        break
print('-=' * 30)
print(f'Você digitou {len(numbers)} elementos.')
numbers.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numbers}')
print('O valor 5 faz parte da lista!') if 5 in numbers else print('O valor 5 não faz parte da lista!')
