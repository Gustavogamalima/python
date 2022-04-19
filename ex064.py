total = c = numero = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero != 999:
        total += numero
        c += 1
print(f'Você digitou {c} números e a soma entre eles foi {total}.')
