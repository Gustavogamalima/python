from random import randint
from time import sleep
player = {}
print('Valores sorteados: ')
for counter in range(1, 5):
    player[f'jogador{counter}'] = randint(1, 6)
    print(f'jogador{counter} tirou {player[f"jogador{counter}"]} no dado.')
    sleep(1)
print('-=' * 30)
print(f'  {" RANKING DOS JOGADORES ":=^27}')
counter = 1
for i in sorted(player, key=player.get, reverse=True):
    print(f'  {counter}º lugar: {i} com {player[i]}.')
    sleep(1)
    counter += 1
