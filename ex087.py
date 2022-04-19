matrix = [[[], [], []], [[], [], []], [[], [], []]]
even = sumOfTheValuesInTheThirdColumn = biggestValueOfSecondLine = 0
for l in range(0, 3):
    for c in range(0, 3):
        value = int(input(f'Digite um valor para [{l}, {c}]: '))
        matrix[l][c].append(value)
        if value % 2 == 0:
            even += value
        if c == 2:
            sumOfTheValuesInTheThirdColumn += value
        if l == 1:
            if value > biggestValueOfSecondLine:
                biggestValueOfSecondLine = value
print('-=' * 30)
print(f'[{matrix[0][0][0]:^5}], [{matrix[0][1][0]:^5}], [{matrix[0][2][0]:^5}]')
print(f'[{matrix[1][0][0]:^5}], [{matrix[1][1][0]:^5}], [{matrix[1][2][0]:^5}]')
print(f'[{matrix[2][0][0]:^5}], [{matrix[2][1][0]:^5}], [{matrix[2][2][0]:^5}]')
print('-=' * 30)
print(f'A soma dos valores pares é {even}')
print(f'A soma dos valores da terceira coluna é {sumOfTheValuesInTheThirdColumn}.')
print(f'O maior valor da segunda lina é {biggestValueOfSecondLine}')
