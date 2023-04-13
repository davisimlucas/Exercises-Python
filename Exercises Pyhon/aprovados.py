'''
Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em um vetor. Depois, imprimir
os nomes dos alunos aprovados, considerando aprovados aqueles cuja média das notas seja maior ou
igual a 6.0 (seis).
'''

N = int(input('Insira a quantidade de alunos: '))

name: str = [0 for x in range(N)]
nota1: float = [0 for x in range(N)]
nota2: float = [0 for x in range(N)]
media: float = [0 for x in range(N)]

for i in range(N):
    name[i] = str(input(f'Insira o nome do {str(i+1)}° aluno: '))
    nota1[i] = float(input(f'Insira a primeira nota do {str(i+1)}° aluno: '))
    nota2[i] = float(input(f'Insira a segunda nota do {str(i+1)}° aluno: '))
    media[i] = float((nota1[i] + nota2[i])/2.0)
print('---------------------------------------')
print('Alunos aprovados:')
for i in range(N):
    if media[i] >= 5:
        print(f'{name[i]} com média de {media[i]}')
print('Alunos reprovados: ')        
for i in range(N):
    if media[i] < 5: 
        print(f'{name[i]} com média de {media[i]}')   



