escolha = 's'
soma = c = maior = 0
while escolha == 's':
    numero = int(input('digite um número: '))
    if c == 0:
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    c += 1
    escolha = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    soma += numero
media = soma / c
print(f'Você digitou {c} número e a média foi {media:.1f}')
print(f'O maior valor foi {maior} e menor foi {menor}')