'''
Ler uma matriz quadrada de ordem N (máximo = 10), contendo números reais. Em seguida, fazer as
seguintes ações:
a) calcular e imprimir a soma de todos os elementos positivos da matriz.
b) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos os elementos desta linha.
c) fazer a leitura do índice de uma coluna da matriz e, daí, imprimir todos os elementos desta coluna.
d) imprimir os elementos da diagonal principal da matriz.
e) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir
a matriz alterada. 
'''
import math

linhas = int(input('Insira quantas linhas terão: '))
colunas = int(input('Insira quantas colunas terão: '))

matriz = []
elemento = [[0 for x in range(colunas)] for x in range(linhas)]

for i_linhas in range(linhas):
    linha = []
    for j_colunas in range(colunas):
        elemento = float(input(f'Insira o elemento [{i_linhas}, {j_colunas}]: '))
        linha.append(elemento)
    matriz.append(linha)    

print()
# realizar a impressão da matriz de um modo matemático
for linha in matriz:    
    print('  '.join(str(i_linhas) for i_linhas in linha))
    # vai percorrer as linhas da matriz separando os elementos (strings) por '  ', 
    #obs: não é necessário colocar pra percorrer colunas, pois for linhas in matriz faz isso.
    '''
    join() => função que realiza a união de strings de acordo com um separador, no exemplo
    é usado '  ' (espaço) como separador.
    '''
print(f'-------------------------\n')
# (a) calcular e imprimir a soma de todos os elementos positivos da matriz.   
maior_ = []
for i_linhas in range(linhas):
    for j_colunas in range(colunas):
        if matriz[i_linhas][j_colunas] > 0:
            maior_.append(matriz[i_linhas][j_colunas])
print(f'(a) A soma dos elementos positivos = {sum(maior_):.1f}\n')

print(f'--------------------------')
# (b) fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos os elementos desta linha.
linha_escolhida = int(input('(b) Digite a linha que você deseja imprimir: '))
linha_esc = []
for j_colunas in range(colunas):
    linha_esc.append(matriz[linha_escolhida][j_colunas])

print(f'A linha escolhida possui os seguintes elementos: {linha_esc}\n')

print(f'--------------------------')
# (c) fazer a leitura do índice de uma coluna da matriz e, daí, imprimir todos os elementos desta coluna.
coluna_escolhida = int(input('(c) Digite a coluna que você deseja imprimir: '))
coluna_esc = []
for i_linhas in range(linhas):
    coluna_esc.append(matriz[i_linhas][coluna_escolhida])

print(f'A coluna escolhida possui os seguintes elementos: {coluna_esc}\n')

print(f'-------------------------\n')
# (d) imprimir os elementos da diagonal principal da matriz.
diag_pricipal = []
for i_linhas in range(linhas):
    for j_colunas in range(colunas):
        if i_linhas == j_colunas:
            diag_pricipal.append(matriz[i_linhas][j_colunas])

print(f'Os elementos diagonal principal são: {diag_pricipal}\n')

print(f'-------------------------\n')
# (e) alterar a matriz elevando ao quadrado todos os números negativos da mesma. Em seguida imprimir a matriz alterada. 
matriz_alteracao = []
for i_linhas in range(linhas):
    linha_alt = []
    for j_colunas in range(colunas):
        if matriz[i_linhas][j_colunas] < 0:
            linha_alt.append(math.pow(matriz[i_linhas][j_colunas], 2.0))
        else: 
            linha_alt.append(matriz[i_linhas][j_colunas])    
    matriz_alteracao.append(linha_alt)       
print()
for linha_alt in matriz_alteracao:
    print('  '.join(str(x) for x in linha_alt))
