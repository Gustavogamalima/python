numeros = (
    int((input('Digite um número: '))),
    int((input('Digite outro número: '))),
    int((input('Digite mais um número: '))),
    int((input('Digite o último número: ')))
)
numPar = 0
for num in numeros:
    if num % 2 == 0:
        numPar += 1
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 aparareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
print(f'Os valores pares digitados foram {numPar}')

