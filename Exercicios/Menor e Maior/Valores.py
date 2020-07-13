resp = 'S'
soma =quant = média = maior =menor =0
while resp in 'Ss':
    núm = int(input('Digite um Valor:'))
    soma +=núm
    quant += 1
    if quant ==1:
        maior = menor =núm
    else:
        if núm > maior:
            maior =núm
        else:
            if núm < menor:
                menor = núm
                #Quando não querer digitar mais valor CLICK 0
                resp = str(input('Quer continuar [S/N] ')).upper().strip()[0]
                media = soma / quant
                print('Você digitou {} numeros e a media foi {}'.format(quant, média))
                print('O maior foi {} e o menor foi {}'.format(maior, menor))