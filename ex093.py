player = {}
player['nome'] = str(input('Nome do jogador: ')).strip().title()
footballMatch = int(input(f'Quantas partidas {player["nome"]} jogou? '))
player['gols'] = []
player['total'] = 0
for counter in range(0, footballMatch):
    player['gols'].append(int(input(f'Quantos gols na partida {counter}? ')))
    player['total'] += player['gols'][counter]
print('-=' * 30)
print(player)
print('-=' * 30)
for key, value in player.items():
    print(f'O campo {key} tem o valor {value}')
print('-=' * 30)
print(f'O jogador {player["nome"]} jogou {footballMatch} partidas.')
for index, value in enumerate(player['gols']):
    print(f'  => Na partida {index}, fez {value} gols.')
print(f'Foi um total de {player["total"]} gols.')