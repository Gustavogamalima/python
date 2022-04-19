people = []
total = averageAge = 0
while True:
    person = {"name": str(input('Nome: ')).strip().title()}
    while True:
        person["sex"] = str(input('Sexo: [M/F] ')).strip().lower()[0]
        if person["sex"] not in 'mf':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            person["age"] = int(input('Idade: '))
            break
    while True:
        answer = str(input('Quer continuar? ')).strip().lower()[0]
        if answer not in 'sn':
            print('ERRO! Responda apenas S ou N.')
        else:
            break
    total += person['age']
    people.append(person.copy())
    if answer == 'n':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(people)} pessoas cadatradas.')
averageAge = total / len(people)
print(f'B) A média de idade é de {averageAge:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for index, value in enumerate(people):
    if value['sex'] == 'f':
        print(value['name'], end=' ')
print('\nD) Lista das pessoas acima da média: ')
for index, value in enumerate(people):
    if value["age"] > averageAge:
        print(f'  nome = {value["name"]}; sexo = {value["sex"]}; idade = {value["age"]}')
print('<<', ' ENCERRADO ', '>>')
