'''
Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.
'''
N = int(input('Inserir a quantidade de números: '))
vetor = []
soma_num = float(0)
for i in range(N):
    v = float(input('Insira um número: '))
    vetor.append(v)
    soma_num =+ vetor[i]
media = float(soma_num /  N)
print(f'A média dos números é de {media:.2f}')
for i in range(N):
    if vetor[i] < media:
        print(vetor[i])





