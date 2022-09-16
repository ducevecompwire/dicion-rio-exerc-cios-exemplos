listaAlunos = []
listaProfessores = []
def menu():
    print('-='*30)
    print('SISTEMA DE CADASTRO DE ALUNOS E PROFESSORES')
    print('-='*30)
    
    print('1 - Cadastrar aluno')
    print('2 - Listar alunos')
    print('3 - Cadastrar Professor')
    print('4 - Listar Professores')
    print('6 - Sair')

def cadastroAluno():
    nome = input('Digite o nome do aluno: ')
    idade = input('Digite a idade do aluno: ')
    curso = input('Digite o curso do aluno: ')
    voltar = input('Deseja voltar ao menu? [S/N] ').upper()
    if voltar == 'S':
        menu()
    else:
        pass
    maisum = input('Deseja cadastrar mais um aluno? [S/N] ').upper()
    if maisum == 'S':
        cadastroAluno()
    else:
        menu()
        
    listaAlunos.append([nome, idade, curso])

def listarAlunos():
    print('-'*30)
    print('LISTA DE ALUNOS')
    for i in listaAlunos:
        print(i)
    voltar = input('Deseja voltar ao menu? [S/N] ').upper()
    if voltar == 'S':
        menu()
    else:
        pass       
def cadastroProfessor():
    nome = input('Digite o nome do professor: ')
    idade = input('Digite a idade do professor: ')
    disciplina = input('Digite a disciplina do professor: ')
    voltar = input('Deseja voltar ao menu? [S/N] ').upper()
    if voltar == 'S':
        menu()
    else:
        pass
    
    maisump = input('Deseja cadastrar mais um professor? [S/N] ').upper()
    if maisump == 'S':
        cadastroProfessor()
    else:
        menu()
    listaProfessores.append([nome, idade, disciplina])
    
def listarProfessores():
    print('-'*30)
    print('LISTA DE PROFESSORES')
    for i in listaProfessores:
        print(i)
    voltar = input('Deseja voltar ao menu? [S/N] ').upper()
    if voltar == 'S':
        menu()
    else:
        pass

while True:
    menu()
    dec = input('Digite a opção desejada: ')
    if dec =='1':
        cadastroAluno()
    elif dec == '2':
        listarAlunos()
    elif dec == '3':
        cadastroProfessor()
    elif dec == '4':
        listaProfessores()
    elif dec == '5':
        menu()
    elif dec == '6':
        break
        
    
    