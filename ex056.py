nome = []
idade = []
sexo = []
total = 0
idadeMax = 0
nomeMax = ''
mulheresM = 0
for c in range(1, 5):
    print(f'---- {c}ª PESSOA -----')
    nome.append(str(input('Nome: ')).strip().lower())
    idade.append(int(input('Idade: ')))
    sexo.append(str(input('Sexo [M/F]: ')).strip().lower())
for c in range(0, len(idade)):
    total += idade[c]
    if idade[c] < 20 and sexo[c] == 'f':
        mulheresM += 1
    if idade[c] > idadeMax and sexo[c] == 'm':
        idadeMax = idade[c]
        nomeMax = nome[c]
media = total / len(idade)
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {idadeMax} anos e se chama {nomeMax.capitalize()}.')
print(f'Ao todo são {mulheresM} mulheres com menos de 20 anos.')
