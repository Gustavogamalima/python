total = menor = mais1000 = c = 0

while True:
    print('-' * 30)
    print(f'{"LOJA SUPER BARATÃO":^30}')
    print('-' * 30)
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    if c == 0:
        menor = preco
        produtoMin = produto
        c += 1
    if preco < menor:
        menor = preco
        produtoMin = produto
    if preco > 1000:
        mais1000 += 1
    total += preco
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont not in 'S':
        break
print(f'{" FIM DO PROGRAMA ":-^30}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f"O produto mais barato foi {produtoMin} que custa R${menor:.2f}")
