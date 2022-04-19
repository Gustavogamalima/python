numbers = []
for c in range(0, 5):
    number = int(input('Digite um valor: '))
    if c == 0 or number > numbers[-1]:
        numbers.append(number)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numbers):
            if number <= numbers[pos]:
                numbers.insert(pos, number)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados foram {numbers}')
