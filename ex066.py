c = soma = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    soma += valor
    c += 1
print(f'A soma dos {c} valores foi {soma}!')
