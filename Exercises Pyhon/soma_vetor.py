'''
Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
- Imprimir todos os elementos do vetor
- Mostrar na tela a soma e a média dos elementos do vetor
'''
n: int 
soma: float; media: float 
n = int(input('Digite a quantidade de números: '))
vetor: int = [0 for x in range(n)]
for i in range(n):
	vetor[i] = float(input('Digite um número: '))
soma = 0
for i in range(n):
	soma =+ vetor[i]
media = soma / n 
for i in range(n):
	print(f'{vetor[i]:.1f}', end='')
print(f'A soma dos números é {soma:.1f}.\nA média dos números é de {media:.2f}.')
