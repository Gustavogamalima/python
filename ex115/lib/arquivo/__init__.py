from ex115.lib.interface import cabeçalho, leiaInt


def criarArquivo(arquivo):
    with open(f'{arquivo}.txt', 'a', encoding='utf-8') as arquivo:
        print(f'Arquivo {arquivo.name} criando com Sucesso!')
    return arquivo


def lerArquivo(arquivo):
    with open(f'{arquivo}.txt', 'r', encoding='latin-1') as arquivo:
        cabeçalho('PESSOAS CADASTRADAS')
        arquivo = arquivo.readlines()
        for itens in arquivo:
            itens = itens.split(';')
            itens[1] = itens[1].replace('\n', '')
            print(f'{itens[0]:<35}{itens[1]:<2} anos')


def cadastroPessoas(arquivo):
    nome = str(input('Nome: ')).strip().title()
    idade = leiaInt('Idade: ')
    with open(f'{arquivo.name}', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome};{idade}\n')
    print(f'Novo registro de {nome} adicionado.')
