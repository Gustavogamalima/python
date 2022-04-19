players = []
while True:
    player = {'nome': str(input('Nome do jogador: ')).strip().title()}
    footballMatch = int(input(f'Quantas partidas {player["nome"]} jogou? '))
    player['gols'] = []
    player['total'] = 0
    for counter in range(0, footballMatch):
        player['gols'].append(int(input(f'Quantos gols na partida {counter}? ')))
        player['total'] += player['gols'][counter]
    players.append(player.copy())
    answer = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if answer == 'N':
        break
print('-=' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":<6}')
print('--' * 30)
for index, value in enumerate(players):
    print(f'{index:<4}{value["nome"]:<15}{str(value["gols"]):<15}{value["total"]:<6}')
print('--' * 30)
while True:
    playerData = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if playerData == 999:
        print('<<', ' VOLTE SEMPRE ', '>>')
        break
    elif playerData > len(players):
        print(f'ERRO! Não existe jogador com código {playerData}!')
        print('--' * 30)
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {players[playerData]["nome"]}; ')
        for index, value in enumerate(players[playerData]["gols"]):
            print(f'  No jogo {index+1} fez {value} gols.')
        print('--' * 30)
