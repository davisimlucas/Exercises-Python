'''
Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto,
mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de
venda das mesmas. Fazer um programa que leia tais dados e determine e escreva quantas mercadorias
proporcionaram:
- lucro < 10%
- 10% ≤ lucro ≤ 20%
- lucro > 20%
Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como
o lucro total.
'''

''' maneira alternativa Chat GPT
nome = [input('Insira o nome da mercadoria: ') for i in range(N)]
compra = [float(input('Insira o preço de compra: ')) for i in range(N)]
venda = [float(input('Insira o preço de venda: ')) for i in range(N)]
'''

# declaração das listas
nome = []
compra = []
venda = []
lucro = []
# declaração dos elementos de cada lista
resposta = str(input('Quer adicionar um produto? '))
N_produtos = 0
while resposta == 'Sim':
    N_produtos =+ 1
    for i in range(N_produtos):
        nome.append(str(input('Insira o nome do produto: ')))
        compra.append(float(input('Insira o preço de compra do produto: R$')))
        venda.append(float(input('Insira o preço de venda do produto: R$')))
        lucro.append(float(((venda[i] / compra[i]) - 1)* 100))
        print()
        resposta = str(input('Quer adicionar outro produto? '))

''' ----> alternativa 
for i in range(N):
    print(f'{i+1}° Produto: ')
    nome.append(input('Insira o nome do produto: '))
    compra_str = input('Insira o preço de compra do produto: ')
    venda_str = input('Insira o preço de venda do produto: ')
    try:
        compra.append(float(compra_str))
        venda.append(float(venda_str))
        lucro.append(float(((venda[i] / compra[i]) - 1)* 100))
    except ValueError:
        print('Valor inválido inserido!')
'''

print('---------------------------------')
contagem_menor10 = 0
contagem_entre10e20 =0 
contagem_maior20 = 0
for i in range(N_produtos):
    print(f'{lucro[i]:.1f}%')
    if lucro[i] < 10: 
        contagem_menor10 =+ 1
    elif lucro[i] >= 10 and lucro[i] < 20:
        contagem_entre10e20 =+ 1
    elif lucro[i] >= 20: 
        contagem_maior20 =+ 1

print('--------------------------------')
print(f'Lucros abaixo de 10%: {contagem_menor10:.1f}\
    \nLucros entre 10% e 20%: {contagem_entre10e20:.1f}\
    \nLucros acima de 20%: {contagem_maior20:.1f}')    # '\' quebra de linha 
print()
lucro_total = float((sum(venda) / sum(compra) - 1)* 100)
print(f'Venda total: R${sum(venda):.1f}\
    \nCompra total: R${sum(compra):.1f}\
    \nLucro total: {lucro_total:.1f}%')
