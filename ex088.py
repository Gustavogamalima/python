from random import randint
from time import sleep
gameDraw = []
numberdrawn = 0
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
answer = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {answer} JOGOS -=-=-=')
for counter in range(1, answer + 1):
    for number in range(0, 6):
        while True:
            numberdrawn = randint(1, 60)
            if numberdrawn not in gameDraw:
                gameDraw.append(numberdrawn)
                break
    print(f'Jogo {counter}: {sorted(gameDraw)}')
    sleep(0.8)
    gameDraw.clear()
print(f'{" < BOA SORTE! > ":=^40}')
