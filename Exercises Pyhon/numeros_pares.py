'''
Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
tela todos os números pares, e também a quantidade de números pares.
'''
n = int(input('Quantos números serão digitados? '))

N: float = [0 for x in range(n)] 

for i in range(n):
    N[i] = float(input(f'Informe o {str(i+1)}º: '))
pares = [x for x in N if x % 2 == 0] 

print(f'Números pares: \n{pares}\nQuantidade de pares: {len(pares)}')   #cod'len' = Return the number of items in a container.

        