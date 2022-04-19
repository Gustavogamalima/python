from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
numeroDoPC = randint(0, 10)
tentativas = 0
numero = int(input('Qual é o seu palpite? '))
while numeroDoPC != numero:
    if numeroDoPC > numero:
        print('Mais... Tente mais uma vez.')
        numero = int(input('Qual é o seu palpite? '))
        tentativas += 1
    else:
        print('Menos... Tente mais uma vez.')
        numero = int(input('Qual é o seu palpite? '))
        tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
