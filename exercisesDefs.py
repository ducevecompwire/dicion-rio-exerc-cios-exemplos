# EXERCÍCIO COM FUNÇÃO  DE ÁREA
"""def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno {larg} x {comp} é de {a}m².', end = ' ')
print('Controle de Terrenos')
print('-' * 30)
perg = str(input('Deseja calcular a área do terreno? [S/N] ')).upper()
if perg == 'S':
    larg = float(input('Largura (m): '))
    comp = float(input('Comprimento (m): '))
    area(larg, comp)
else:
    print('Ok, até mais!')"""

# EXERCÍCIO COM UM PRINT ESPECIAL

"""def escreva(txt):
    print(len(txt) * '-')
    print(txt)
    print(len(txt) * '-')
escreva('Olá, Mundo!')
escreva('Hello Word!')
escreva('Eduardo Ceve da Silva!')"""

# FUNÇÃO DE CONTADOR
'''from time import sleep


print('-=' * 30)
print("Bem vindo ao sistema de contador!")
print('Logo a baixo, vai escolher o início do contador.')
print('Em seguida, vai escolher o fim do contador.')
print("E por fim, vai escolher o passo do contador.")
print("Vamos começar!")


inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

def contador(inicio, fim, passo):
    print(f'Contage de {inicio} até {fim} de {passo} em {passo}.')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end=' ', flush=True) # flush=True, serve para não dar um espaço entre os números.
            sleep(0.5)
            cont -= passo
        print('FIM!')   

        
        
        
contador(inicio, fim, passo)'''

# FUMÇÃO PARA VOTAÇÃO

'''ano = int(input('Em que ano você nasceu? '))

def voto(ano):
    from datetime import date
    date = date.today().year
    date = date - ano
    
    print('-' * date)
    if date < 16 :
        print(f'Com {date} anos: NÃO VOTA.')
    elif date >= 16 and date < 18 :
        print(f'Com {date} anos: VOTO OPCIONAL.')
    elif date >= 18 and date < 65 :
        print(f'Com {date} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {date} anos: VOTO OPCIONAL.')
        
voto(ano)'''
     
# FUNÇÃO PARA CALCULAR FATORIAL

'''def fatorial(n, show = False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
            
        f *= c
    return f
        
print(fatorial(5, show=True))'''

# FUNÇÃO PARA FICHA DO JOGADOR

'''def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} fez {gols} gols no campeonato.')   
    
nome = str(input('Nome do jogador: '))
gols = int(input('Número de gols: '))
ficha(nome, gols) '''

#FUNÇÃO PARA VALIDAR NÚMERO:

'''def leiaInt (msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''

#FUNÇÃO NOTAS E SITUAÇÃO


    