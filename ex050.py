resultado = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        resultado += n
print(f'O resultado da soma dos número pares é: {resultado}')
