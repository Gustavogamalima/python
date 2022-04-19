distancia = float(input('Qual a distância da sua viagem? '))
print(f'Você está preste a começar uma viagem de {distancia}Km.')
print(f'E o preço da sua pasagem será de R${distancia * 0.50 if distancia <= 200 else distancia * 0.45:.2f}')
