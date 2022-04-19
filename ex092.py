from datetime import datetime
people = {'nome': str(input('Nome: ')).strip().title(),
          'idade': datetime.now().year - int(input('Ano de Nascimento: ')),
          'ctps': int(input('Carteira de Trabalho (0 não tem): '))}
if people['ctps'] != 0:
    people['contratação'] = int(input('Ano de Contratação: '))
    people['salário'] = float(input('Salário: R$'))
    people['aposentadoria'] = (35 - (datetime.now().year - people['contratação'])) + people['idade']
print('-=' * 30)
for key, value in people.items():
    print(f'  - {key} tem o valor {value}')
