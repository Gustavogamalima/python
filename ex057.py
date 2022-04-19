sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'M F':
    print(sexo)
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso')