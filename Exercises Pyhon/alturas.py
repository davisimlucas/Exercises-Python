'''
Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
bem como os nomes dessas pessoas caso houver. 
'''
n = int(input('Quantas pessoas serão digitadas: '))

nome: str = [for x in range(n)]
idade: int = [for y in range(n)]
altura: float = [for z in range(n)]

soma_altura = 0
n_menores = 0 

for i in range(n):
    print('Digite os dados da pessoa: ')
    nome[i] = str(input('Digite o nome: '))
    idade[i] = int(input('DIgite a idade: '))
    if idade[i] < 16:
        n_menores =+ 1
    altura[i] = float(input('Digite a altura: '))
    soma_altura =+ altura[i]

media_altura = float(soma_altura / n)

print('------------------------------------------------------\n')
print(f'A média da alturas é de {media_altura:.2f}')

porcent_menores = float((n - n_menores) / n )
print(f'A porcentagem de menores é de {porcent_menores:.2f}%')

for i in range(n):
    if idade[i] < 16:
        print(nome[i])
