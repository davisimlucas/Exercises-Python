'''
Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros
e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos. 
'''
n = int(input('Digite quantos números serão digitados: '))
v: int = [0 for x in range(n)]         #List Comprehension
for i in range(n):
    v[i] = int(input('Digite um número: '))
print('Números negativos: ')
for i in range(n):
    if v[i] < 0: 
        print(v[i])


