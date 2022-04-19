import random
import time

print('''Suas opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
if jogada == 0:
    jogada = 'Pedra'
elif jogada == 1:
    jogada = 'Papel'
else:
    jogada = 'Tesoura'
pc = random.randint(0, 2)
if pc == 0:
    pc = 'Pedra'
elif pc == 1:
    pc = 'Papel'
else:
    pc = 'Tesoura'
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
print('-='*20)
print(f'Computador jogou {pc}')
print(f'Jogador jogou {jogada}')
print('-='*20)
if jogada == 'Pedra' and pc == 'Tesoura' or jogada == 'Papel' and pc == 'Pedra' or jogada == 'Tesoura' and pc == 'Papel':
    print('JOGADOR VENCE')
elif jogada == pc:
    print('JOGO EMPATOU')
else:
    print('COMPUTADOR GANHOU')
