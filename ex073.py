brasileiro = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
              'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
              'Atletico-GO', 'Santos', 'Ceará', 'Internacional',
              'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
              'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-=' * 20)
print(f'Lista dos times do Brasileirão: {brasileiro}')
print('-=' * 20)
print(f'Os 5 primeiros são {brasileiro[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {brasileiro[-4:]}')
print('-=' * 20)
print(f'Os times ordem alfabética: {sorted(brasileiro)}')
print('-=' * 20)
print(f'O Chapecoense está na {brasileiro.index("Chapecoense") + 1}ª posição')
