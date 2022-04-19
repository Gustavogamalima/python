import random

list = []
list.append(str(input('Primeiro aluno: ')))
list.append(str(input('Segundo aluno: ')))
list.append(str(input('Terceiro aluno: ')))
list.append(str(input('Quarto aluno: ')))


print(f'O aluno escolhido foi {list[random.randint(0, list.__len__())]}')
