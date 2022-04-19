maior = homens = mulherJovem = 0
while True:
    print(f"{'CADASTRE UMA PESSOA':^30}")
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulherJovem += 1
    print('-' * 30)
    cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-' * 30)
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadrastados')
print(f'E temos {mulherJovem} mulheres com menos de 20 anos')
