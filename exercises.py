#EXERCÍCIO 01 ->    DICIONÁRIO 

"""aluno = {}
aluno['nome'] = str(input("Digite o nome do aluno: "))
aluno['media'] = float(input("Digite a média do aluno: "))
if aluno['media'] >= 7 :
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')"""""

#EXERCÍCIO 02 -> JOGO DE DADOS 

"""from random import randint
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
    sleep(1)"""
    
#EXERCÍCIO 03 -> CADASTRANDO USUÁRIO EM UM DICIONÁRIO COM UMA PEQUENA CONDIÇÃO

"""from datetime import datetime


cadastro = {}

cadastro['Nome'] = str(input('Digite seu nome: '))
cadastro['idade '] = int(input('Digite o ano em que nasceu: '))
idade = 2022 - cadastro['idade ']
cadastro['idade '] = idade
cadastro['ctps '] = int(input('Digite o número da sua carteira de trabalho (Caso não tenha, digite 0): '))
if cadastro['ctps '] == 0:
    cadastro.update({'ctps': 'Não possui carteira de trabalho.'}) 
    print('-=' * 35)
    for k,v in cadastro.items():
        print(f'-{k} tem o valor de {v}')
    
else:
    cadastro['Ano de contratação'] = int(input('Qual foi o ano da sua contratação: '))
    cadastro['Salário '] = int(input('Qual é o salário que você recebe: '))
    cadastro['aposentadoria'] = ((cadastro['Ano de contratação'] + 35) - datetime.now().year)
    print('-=' * 35)
    for k,v in cadastro.items():
        print(f'-{k} tem o valor de {v}')"""
        
# EXERCÍCIO 04 -> CADASTRO DE JOGADOR DE FUTEBOL



jogador = {}
gols = []
jogador['nome'] = str(input('Qual o nome do jogador?: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))
for i in range(0, partidas):
    cont = 1
    cont = cont + i
    partida = int(input(f'Quantos gols na {cont}ª partida? : '))
    gols.append(partida)
    partida += partida
    jogador['gols'] = gols
    jogador['Total'] = partida
    
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i}, marcou {v} gols. ')
print(f'Foi um total de {jogador["Total"]} gols.')
