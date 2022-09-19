# EXERCÍCIO COM FUNÇÃO  DE ÁREA
def area(larg, comp):
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
    print('Ok, até mais!')    