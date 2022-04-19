from random import randint

n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
numeros = (n1, n2, n3, n4, n5)
print(f'Os valores sorteados foram: {numeros[0]} {numeros[1]} {numeros[2]} {numeros[3]} {numeros[4]}')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
