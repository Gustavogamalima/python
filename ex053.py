frase = str(input('Digite uma frase: ')).strip().upper()
frase = ''.join(frase.split())
fraseInvertida = ''.join(frase[len(frase)::-1])
print(f'O inverso de {frase} é {fraseInvertida}')
if frase != fraseInvertida:
    print('A frase digitada não é um palíndromo!')
else:
    print('A frase digitada é um palíndromo!')
