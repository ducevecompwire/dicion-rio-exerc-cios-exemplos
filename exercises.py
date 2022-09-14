#EXERCÍCIO 01

aluno = {}
aluno['nome'] = str(input("Digite o nome do aluno: "))
aluno['media'] = float(input("Digite a média do aluno: "))
if aluno['media'] >= 7 :
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')

#EXERCÍCIO 02

