#EXERCÍCIO 01

"""aluno = {}
aluno['nome'] = str(input("Digite o nome do aluno: "))
aluno['media'] = float(input("Digite a média do aluno: "))
if aluno['media'] >= 7 :
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')"""""

#EXERCÍCIO 02

from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1' : randint(1,6),
    'jogador2' : randint(1,6),
    'jogador3' : randint(1,6),
    'jogador4' : randint(1,6),}
ranking = []
print('Valores sorteados: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar {v[0]} com {v[1]}.')
    sleep(1)