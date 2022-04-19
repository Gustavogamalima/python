numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
'''
)
opcao = int(input('Sua opção: '))
if opcao == 1:
    tipo = 'BINÁRIO'
    resultado = str(bin(numero))
elif opcao == 2:
    tipo = 'OCTAL'
    resultado = str(oct(numero))
elif opcao == 3:
    tipo = 'HEXADECIMAL'
    resultado = str(hex(numero))
else:
    print('Opção inválida. Tente novamente.')
    exit()
print(f'{numero} convertido para {tipo} é igual a {resultado[2:]}')