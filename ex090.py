student = {}
student['nome'] = str(input('Nome: ')).strip().title()
student['média'] = float(input(f'Média de {student["nome"]}: '))
if student['média'] >= 7:
    student['situação'] = 'Aprovado'
elif student['média'] >= 5:
    student['situação'] = 'Recuperação'
else:
    student['situação'] = 'Reprovado'
print('-=' * 30)
for key, value in student.items():
    print(f'  - {key} é igual a {value}')
