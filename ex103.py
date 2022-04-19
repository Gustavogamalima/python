def playerPresentation(n='<desconhecido>', gols: object = 0) -> object:
    print(f'O jogador {n} fez {gols} gol(s) no campeonato.')


print('-' * 30)
name = str(input('Nome do Jogador: ')).strip().title()
goalsNumbers = str(input('Número de Gols: '))
if name is not name.isalnum():
    if goalsNumbers is not goalsNumbers.isnumeric():
        playerPresentation()
    else:
        playerPresentation(gols=goalsNumbers)
elif name is name.isalnum():
    if goalsNumbers is not goalsNumbers.isnumeric():
        playerPresentation(n=name)
    else:
        playerPresentation(n=name, gols=goalsNumbers)
