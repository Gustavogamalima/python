from time import sleep


def larger(*number):
    print('-=' * 30)
    print('Analizando os valores passados...')
    for index, value in enumerate(number):
        sleep(0.4)
        print(value, end=' ')
    print(f'Foram informados {len(number)} valores ao todo.')
    if number == ():
        number = 0
    print(f'O maior valor informado foi {number}.')


larger(2, 9, 4, 5, 7, 1)
larger(4, 7, 0)
larger(1, 2)
larger(6)
larger()
