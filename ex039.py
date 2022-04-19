from datetime import datetime

anoNasc = int(input('Ano de nascimento: '))
anoAtual = datetime.now().year
idade = anoAtual - anoNasc

print(f'Quem nasceu em {anoNasc} tem {idade} anos em {anoAtual}.')
if idade < 18:
    idadeQueFalta = 18 - idade
    print(f'Ainda faltam {idadeQueFalta} anos para o alistamento')
    print(f'Seu alistamento será em {anoAtual + idadeQueFalta}')
elif idade > 18:
    idadeAMais = idade - 18
    idadeAlistar = anoNasc + 18
    print(f'Você já deveria ter se alistado há {idadeAMais} anos')
    print(f'Seu alistamento foi em {idadeAlistar}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
