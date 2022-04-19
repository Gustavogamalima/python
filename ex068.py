from random import randint
venceu = 0
resultado = 'DEU PAR'
while True:
    print('=-' * 20)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-' * 20)
    valor = int(input('Diga um valor: '))
    pcValor = randint(0, 10)
    parImpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('--' * 20)
    total = pcValor + valor
    if total % 2 != 0:
        resultado = 'DEU ÍMPAR'
    print(f'Você jogou {valor} e o computador {pcValor}. Total de {total} {resultado}')
    print('--' * 20)
    if parImpar == 'I' and total % 2 == 0 or parImpar == 'P' and total % 2 != 0:
        print(f'Você PERDEU!')
        break
    elif parImpar == 'P' and total % 2 == 0 or parImpar == 'I' and total % 2 != 0:
        print('Você VENCEU!')
        venceu += 1
        print('Vamos jogar novamente...')
    elif parImpar not in 'PI':
        print('Valor inválido!')
        print(f'Você PERDEU!')
        break
print('=-' * 20)
print(f'GAME OVER! Você venceu {venceu} vezes.')