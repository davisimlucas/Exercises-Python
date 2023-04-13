#Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo.
n: int; N: int
T = int(input('Digite o número que será a tabuada: '))
N = int(input('Qual será o número de repetições? '))
for n in range(N+1):
    x = int(n * T)
    print(f'{n} x {T} = {x}')