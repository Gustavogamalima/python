print('''========== LOJAS GUANABARA ==========''')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    desconto = preco - (preco * 0.1)
    print(f'Sua compra de R${preco:.2f} vai custar R${desconto} no final.')
elif opcao == 2:
    desconto = preco - (preco * 0.05)
    print(f'Sua compra de R${preco:.2f} vai custar R${desconto} no final.')
elif opcao == 3:
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2x de {parcela:.2f} SEM JUROS')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preco * 1.2
    parcela = juros / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de {parcela:.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${juros} no final.')
else:
    print('Opção inválida de pagamento.')