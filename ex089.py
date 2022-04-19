people = []
person = []
name = []
schoolGrades = []
schoolAverage = 0
while True:
    name.append(str(input('Nome: ')).strip().capitalize())
    schoolGrades.append(float(input('Nota 1: ')))
    schoolGrades.append(float(input('Nota 2: ')))
    person.append(name[:])
    person.append(schoolGrades[:])
    people.append(person[:])
    name.clear()
    schoolGrades.clear()
    person.clear()
    answer = str(input('Quer continuar? [S/N] ')).strip().lower()
    if answer == 'n':
        break
print('-=' * 30)
print(f'Nº {"Nome":<20}{"Média":<7}')
print('-' * 30)
for index, person in enumerate(people):
    schoolAverage = (int(person[1][0]) + int(person[1][1])) / 2
    print(f'{index}  {person[0][0]:<15}{schoolAverage:>8}')
print('-' * 40)
while True:
    studentGrades = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if studentGrades == 999:
        print('FINALIZANDO...')
        print('<' * 3, 'VOLTE SEMPRE', '>' * 3)
        break
    print(f'Notas de {people[studentGrades][0][0]} são {people[studentGrades][1]}')
    print('-' * 40)
