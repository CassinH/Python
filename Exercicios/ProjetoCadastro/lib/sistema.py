from ProjetoCadastro.lib.interface import *
from ProjetoCadastro.lib.arquivo import *
from time import sleep

cabeçalho('SISTEMA ARQUIVO v1.0')

# Ter uma Opção de criar um arquivo
arq ='ArquivoSistema.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


    print('Arquivo encontrado com Sucesso!' )
else:
    print('Arquivo não encontrado!')


while True:
    reposta = menu(['Listar Pessoas', 'Cadastrar Pessoa','Sair do Sistema'])
    # Opção de listar um item do arquivo
    if reposta==1:
        lerArquivo(arq)
    elif reposta==2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome =str(input('Nome: '))
        idade=leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
        #Opção de listar a lista
    elif reposta==3:
        #Opção de sair do Sistema
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep('1')





