numero = int(input('Digite um número para \ncalcular seu Fatorial: '))
print(f'Calculando {numero}! =', end='')
cont = numero
resultado = 1
while cont >= 1:
    resultado = resultado * cont
    if cont == 1:
        print(f' {cont} = {resultado}', end='')
    else:
        print(f' {cont} x', end='')
    cont -= 1



