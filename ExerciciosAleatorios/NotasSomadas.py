n1=float(input('Nota do Primeiro Semestre...ALUNO 1: '))
n2=int(input('Nota do Segundo Semestre...ALUNO 1: '))
n3=int(input('Nota do Terceiro Semestre...ALUNO 1: '))
n4=int(input('Nota do Quarto Semestre...ALUNO 1: '))

soma=(n1+n2+n3+n4)
resutado=soma/2


print('Resultado de todas as Notas {}'.format(soma),'é a media {}'.format(resutado))

if soma < 60:
    print('Reprovado')
elif soma<100:
    print('Aprovado')
else:
    print('Aprovado com Distinção!')


