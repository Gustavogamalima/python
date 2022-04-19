escolha = 0
pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
while escolha != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
    ''')
    escolha = int(input('Qual é a sua opção? '))
    if escolha == 1:
        print(f'A soma entre {pv} + {sv} é {pv + sv}')
        print('=-' * 30)
    elif escolha == 2:
        print(f'A multiplicação entre {pv} x {sv} é {pv * sv}')
        print('=-' * 30)
    elif escolha == 3:
        if pv > sv:
            maior = pv
        else:
            maior = sv
        print(f'Entre {pv} e {sv} o maior valor é {maior}')
        print('=-' * 30)
    elif escolha == 4:
        print('Informe os números novamente:')
        pv = int(input('Primeiro valor: '))
        sv = int(input('Segundo valor: '))
        print('=-' * 30)
    elif escolha == 5:
        print('Finalizando...')
        print('=-' * 30)
    else:
        print('Opção inválida. Tente novamente')
        print('=-' * 30)
