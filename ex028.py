from random import randint
from time import sleep

print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*30)
numero = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
numeroDoPC = randint(0, 5)
if numero == numeroDoPC:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {numeroDoPC} e não no {numero}!')

