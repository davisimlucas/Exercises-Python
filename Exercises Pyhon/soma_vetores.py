'''
Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
o vetor C gerado. 
'''
n = int(input('Informe qual será o tamanho de cada vetor '))
A = []
B = []
C = []
for i in range(n):
    a = float(input('Digite um número: '))
    A.append(a)
print(A)
for i in range(n):
    b = float(input('Digite um número: '))
    B.append(b)
print(B)
for i in range(n):
    C.append(A[i] + B[i])
print(F'VETOR RESULTANTE\n{C}')
