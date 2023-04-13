'''
Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
da pessoa mais velha.
'''
N = int(input('Insira o números de pessoas: '))

name: str = [0 for x in range(N)]   # list 
age: int = [0 for x in range(N)]    # list

for i in range(N):
    name[i] = input(f'Digite o nome da {i+1}° pessoa: ')
    age[i] = input(f'Digite a idade da {i+1}° pessoa: ')

for i in range(N):
    if age[i] == min(age):   # min(list): busca o menor número da lista
        print(f'\nPessoa mais nova: {name[i]}\n')   
