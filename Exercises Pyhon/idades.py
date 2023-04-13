'''
Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
nomes e a idade média entre essas pessoas, com uma casa decimal
'''
nome1 = str; nome2 = str
idade1 = int; idade2 = int
idade_media = float

print('Digite os dados da primeira pessoa: ')
nome1 = str(input('Nome da primeira pessoa: '))
idade1 = int(input('Idade da primeira pessoa: '))

print('Digite os dados da segunda pessoa: ')
nome2 = str(input('Nome da segunda pessoa: '))
idade2 = int(input('Idade da segunda pessoa: '))

idade_media = (idade1 + idade2) / 2
print(f'Os nomes das pessoas em questão são {nome1} e {nome2}, e a idade média entre elas é de {idade_media}')
