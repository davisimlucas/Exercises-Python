'''
Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
considerando a primeira posição como 0 (zero). 
'''
n = int(input('Informe quantos números serão digitados: '))

vetor = []  #list
for i in range(n):
    numero = float(input('Digite um número: '))
    vetor.append(numero)
maior = max(vetor)
posicao = vetor.index(maior)

print(f'O maior número é {maior:.1f}.\nO maior número está na posição {str(posicao)}')