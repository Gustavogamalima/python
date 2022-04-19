from time import sleep


def score(n1, n2, j):
    if j == 0:
        j = 1
    print('-=' * 20)
    print(f'Contagem de {n1} até {n2} de {j} em {j}')
    if n1 > n2:
        if j > 0:
            j = -j
        n2 -= 2
    for counter in range(n1, n2 + 1, j):
        sleep(0.3)
        print(counter, end=' ')
    print('FIM!')


score(1, 10, 1)
score(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
start = int(input(f'{"Início:":<8}'))
end = int(input(f'{"Fim:":<8}'))
jump = int(input(f'{"Passo:":<8}'))
score(start, end, jump)
print('-=' * 20)
