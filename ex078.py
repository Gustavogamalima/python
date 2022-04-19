lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-' * 30)
print(f'Você digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, numero in enumerate(lista):
    if numero == maior:
        print(pos, end='... ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos, numero in enumerate(lista):
    if numero == menor:
        print(pos, end='... ')
