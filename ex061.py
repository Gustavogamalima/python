print('Gerador de PA')
print('-=' * 20)
pt = int(input('Primeiro termo: '))
st = int(input('Razão da PA: '))
c = 0
resultado = pt
while c < 10:
    if c == 0:
        print(f'{pt} -> ', end='')
    else:
        resultado += st
        print(f'{resultado} -> ', end='')
    c += 1
print('FIM')