nomeCompleto = str(input('Digite seu nome completo: ')).strip()
print('Analizando seu nome...')
print(f'Seu nome em maiúsculas é {nomeCompleto.upper()}')
print(f'Seu nome em letras minúsculas é {nomeCompleto.lower()}')
print(f'Seu nome tem ao todo {"".join(nomeCompleto.split()).__len__()} letras')
primeiroNome = nomeCompleto.split()[0]
print(f'Seu primeiro nome é {primeiroNome} e ele tem {primeiroNome.__len__()}')
