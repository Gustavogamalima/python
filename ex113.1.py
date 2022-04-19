def readInteger(text):
    while True:
        try:
            number = int(input(text))
        except:
            print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[;1m')
        else:
            return number
            break


def readFloat(text):
    while True:
        try:
            number = float(input(text))
        except:
            print(f'\033[1;31mERRO: por favor, digite um número real válido.\033[;1m')
        else:
            return number
            break


numeroInteiro = readInteger('Digite um número Inteiro: ')
numeroReal = readFloat('Digite um número Real: ')

print(
    f'O valor inteiro digitado foi {numeroInteiro} e o real foi {numeroReal}')
