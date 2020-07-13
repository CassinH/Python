print(' {:=^40} ' .format('LOJA CASSIO' ))
preço=float(input('Preço das compras: R$'))

#ESCOLHER FORMAS DE PAGAMENTOS
print('''FORMAS DE PAGAMENTO
[1] à vista DINHEIRO
[2] à vista CARTÃO 
[3]  à vista CHEQUE
[4] 2X no CARTÃO
[5] 3x ou mais VEZS NO CARTÃO''')
opção=int(input('QUAL É A MELHOR OPÇÃO '))

#DESCONTO DE 10%
if opção==1:
    total=preço -(preço*10/100)
    print('O valor do item da sua compra foi R${:.2f}'.format(preço))
    print('O valor da sua compra com desconto 10% foi R${:.2f} '.format(total))
#DESCONTO DE 5%
elif opção ==2:
    total = preço - (preço * 5/ 100)
    print('Sua compra de R${:.2f} vai custar com os 5% foi R${:.2f} no final.'.format(preço,total))
#DESCONTO DE 3%
elif opção==3:
    total = preço - (preço * 3 / 100)
    print('O valor do item da sua compra foi R${:.2f}'.format(preço))
    print('O valor da sua compra com desconto 3% foi R${:.2f} '.format(total))
#DIVIDDINDO EM 2X
elif opção==4:
    total=preço
    parcela=total/2
    print('Sua compra foi parcelada em 2x de R${:.2f}'.format(parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço,total))
#DIVIDINDO EM MAIS VEZES COM JUROS DE 20%
elif opção==5:
    total=preço+(preço*20/100)
    totalparc=int(input('Quantas parcelas?'))
    parcela=total/totalparc
    print('Sua compra será parcela em {}x de R${:.2f} JUROS'.format(totalparc,parcela))
    print('SUa compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço,total))