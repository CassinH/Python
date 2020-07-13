n1=int(input('Digite o Segundo Valor?'))
n2=int(input('Digite o Segundo Valor?'))
opção=0
while opção !=5:
    print('''[1]somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] Sair do programa''')
    opção = str(input('Qual é a sua opção?'))
    if opção == 1:
        soma =n1+n2
        print('Soma entre {} e {} é {}'.format(n1,n2,soma))
    elif opção == 2:
        produto =n1*n2
        print('Resultado entre {} e {} é {}'.format(n1, n2,produto))
    elif opção == 3:
        if n1>n2:
            maior =n1
        else:
            maior=n2
            print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
    elif opção == 4:
        print('Informe novamente os numeros:')
        n1= int(input('Digite primeiro numero'))
        n2 = int(input('Segunda primeiro numero'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida.Tente novamente')
        print('=-='*30)
    print('Fim do programa! Volte sempre!')

