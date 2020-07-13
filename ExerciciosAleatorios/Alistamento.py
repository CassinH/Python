from datetime import date
atual=date.today().year
nascimento=int(input('Ano de Nascimento: '))
idade=atual-nascimento
print('Quem nasceu em {} tem {} anos em {} '.format(nascimento,idade,atual))
if idade==18:
    print('Você tem que alistar IMEDIATAMENTE!')
elif idade<18:
    saldo = 18- idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano=atual+saldo
    print('Seu alistamento será em {}' .format(ano))
elif idade>18:
    saldo=idade-18
    print('Vocé ja deveria ter se ALISTADO há {}'.format(saldo))
    ano=atual-saldo
    print('Seu Alistamento foi em {}'.format(ano))