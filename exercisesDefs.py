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
from time import sleep


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

        
        
        
contador(inicio, fim, passo)
    
     
        