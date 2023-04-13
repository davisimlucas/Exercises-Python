'''
Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
de homens.
'''

N = int(input('Insira o número de pessoas: '))

#declaração das váriáveis 
altura: float = [0 for x in range(N)]
altura_F: float = [0 for x in range(N)]
genero: str = [0 for x in range(N)]

#input de todos os dados
for i in range(N):
    print(f'Dados da {str(i+1)}° pessoa: ')
    altura[i] = float(input('Insira a altura da pessoa: '))
    genero[i] = str(input('Insira o gênero da pessoa: '))
    while genero[i] != 'M' and genero[i] != 'F':
            print('Resposta não aceita. Tente novamente')
            genero[i] = str(input('Insira o gênero da pessoa: '))

# print da maior e menor altura:
print(f'\nMaior altura: {max(altura)}\nMenor altura: {min(altura)}')

#cálculo da média de altura entre mulheres:
for i in range(N):
    if genero[i] == 'F':
        altura_F[i] = altura[i]
        media_alt_F = float(sum(altura_F)/(float(N - int(genero.count('M')))))
print(f'A média de altura entre mulheres é de {media_alt_F:.2f}m.')

#print do número de homens 
print('Número de homens: ', genero.count('M'))
