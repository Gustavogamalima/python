numbers = []
even = []
odd = []
while True:
    numbers.append(int(input('Digite um número: ')))
    desire = str(input('Quer continuar? ')).strip().lower()[0]
    if desire == 'n':
        break
print('-=' * 30)
print(f'A lista completa é {numbers}')
for value in numbers:
    even.append(value) if value % 2 == 0 else odd.append(value)
print(f'A lista de pares é {even}')
print(f'A lista de ímpares é {odd}')
