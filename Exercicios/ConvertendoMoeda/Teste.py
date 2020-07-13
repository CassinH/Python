from ConvertendoMoeda import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${p} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumento(p,10))}')