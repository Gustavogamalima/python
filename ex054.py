from datetime import datetime

contAdulto = 0
contMenores = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = datetime.now().year - ano
    if idade >= 21:
        contAdulto += 1
    else:
        contMenores += 1
print(f'Ao todo tivemos {contAdulto} pessoas maiores de idade')
print(f'E também tivemos {contMenores} pessoas menores de idade')

