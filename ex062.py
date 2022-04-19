print('Gerador de PA')
print('-=' * 20)
pt = int(input('Primeiro termo: '))
st = int(input('Razão da PA: '))
c = 0
total = 0
quantidade = 10
resultado = pt
while quantidade > 1:
    while c < quantidade:
        if c == 0:
            print(f'{pt} -> ', end='')
        else:
            resultado += st
            print(f'{resultado} -> ', end='')
        c += 1
        if c == quantidade:
            pt = resultado + st
            resultado = pt
            total += c
            c = 0
            print('PAUSA')
            quantidade = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')