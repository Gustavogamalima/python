print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
termos = int(input('Quantos termos você quer mostrar? '))
c = 0
pt = 0
st = 1
print('~~' * 10)
while c < (termos / 2):
    print(f'{pt} -> ', end='')
    print(f'{st} -> ', end='')
    c += 1
    pt = pt + st
    st = pt + st
print('FIM')
print('~~' * 10)
