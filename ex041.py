from datetime import datetime

ano = int(input('Ano de Nascimento: '))
idade = datetime.now().year - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    classificacao = 'Mirim'
elif idade <= 14:
    classificacao = 'Infantil'
elif idade <= 19:
    classificacao = 'Junior'
elif idade <= 25:
    classificacao = 'Sênior'
else:
    classificacao = 'Master'
print(f'Classificação: {classificacao}')
