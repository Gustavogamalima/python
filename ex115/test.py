from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arquivoTxt = 'cursoemvideo'
arquivo = criarArquivo(arquivoTxt)
while True:
    resposta = menu(['Ver pessoas cadastra', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arquivoTxt)
    elif resposta == 2:
        cadastroPessoas(arquivo)
    elif resposta == 3:
        cabeçalho('Saindo do Sitema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)
