pn = float(input('Primeira nota: '))
sn = float(input('Segunda nota: '))
media = (pn + sn) / 2
print(f'Tirando {pn:.1f} e {sn:.1f}, a média do aluno é {media:.1f}')
if media < 5:
    print('O aluno está REPROVADO.')
elif media < 7:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO.')