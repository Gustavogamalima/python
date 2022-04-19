from random import randint
from time import sleep


def randomValues():
    numbers = []
    for counter in range(0, randint(1, 10)):
        numbers.append(randint(1, 10))
    print(f'Sorteando {len(numbers)} valores da lista:', end=' ')
    for value in numbers:
        print(value, end=' ')
        sleep(0.3)
    print('PRONTO!')
    return numbers


def sumOfEvenValues(numbers):
    result = 0
    for value in numbers:
        if value % 2 == 0:
            result += value
    print(f'Somando os valores pares de {numbers}, temos {result}')


sumOfEvenValues(randomValues())
