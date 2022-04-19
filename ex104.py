def readInteger(text):
    while True:
        number = str(input(text)).strip()
        if number.isnumeric():
            number = int(number)
            return number
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[;1m')


n = readInteger('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
