people = []
person = []
greaterWeight = lessWeight = amountOfPeople = 0
namesOfTheHeaviest = []
namesOfTheLightest = []
weights = []
while True:
    person.append(str(input('Nome: ')).strip().capitalize())
    person.append(float(input('Peso: ')))
    amountOfPeople += 1
    people.append(person[:])
    desire = str(input('Quer continuar? ')).strip().lower()[0]
    person.clear()
    if desire == 'n':
        break
for name, value in people:
    weights.append(value)
greaterWeight = max(weights)
lessWeight = min(weights)
for index, value in enumerate(people):
    if value.count(greaterWeight) == 1:
        namesOfTheHeaviest.append(value[0])
    if value.count(lessWeight) == 1:
        namesOfTheLightest.append(value[0])
print('-=' * 30)
print(f'Ao todo, você foi cadastrou {amountOfPeople} pessoas.')
print(f'O maior peso foi de {greaterWeight}Kg. Peso de {namesOfTheHeaviest}')
print(f'O menor peso foi de {lessWeight}Kg. Peso de {namesOfTheLightest}')
