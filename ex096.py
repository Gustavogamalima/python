def area(a, b):
    print(f'A área de um terreno {a}x{b} é de {a * b}m².')


print(' Controle de Terrenos ')
print('----------------------')
width = float(input('LARGURA (m): '))
length = float(input('COMPRIMENTO (m): '))
area(width, length)
