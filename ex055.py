pesoMax = 0
pesoMin = 1000
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if peso > pesoMax:
        pesoMax = peso
    elif peso < pesoMin:
        pesoMin = peso
print(f'O maior peso lido foi de {pesoMax:.1f}Kg')
print(f'O menor peso lido foi de {pesoMin:.1f}Kg')
