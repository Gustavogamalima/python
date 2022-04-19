n = str(input('Digite um número entre 0 e 9999: ')).strip()
print(f'Analisando o número {n}')
n = list(n)
n0 = ['0', '0', '0', '0']
n0[len(n):] = n
print(f'Unidade: {n0[-1]}')
print(f'Dezena: {n0[-2]}')
print(f'Centena: {n0[-3]}')
print(f'Milhar: {n0[-4]}')

