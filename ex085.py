numbers = [[], []]
for c in range(0, 7):
    value = int(input(f'Digite o {c + 1}ª valor: '))
    numbers[0].append(value) if value % 2 == 0 else numbers[1].append(value)
print('-=' * 30)
print(f'Os valores ímpares digitados foram: {sorted(numbers[1])}')
print(f'Os valores pares digitados foram: {sorted(numbers[0])}')
