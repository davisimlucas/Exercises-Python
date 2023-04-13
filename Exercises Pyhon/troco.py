'''
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente.
'''
preco_produto: float; valor_pago: float; troco: float; valor_total: float; valor_falta: float
quantidade_comprada: int

preco_produto = float(input('Digite o preço do produto: '))
quantidade_comprada = int(input('Digite a quantidade de produto comprada: '))
valor_pago = float(input('Digite o valor pago: '))
valor_total = quantidade_comprada * preco_produto
valor_falta = valor_total - valor_pago
troco = valor_pago - valor_total

if valor_pago < valor_total:
    print(f'Valor insuficiente, por favor pagar R${valor_falta:.2f}')
else:
    print(f'O preço do produto é de R${preco_produto:.2f}, sendo comprado {quantidade_comprada} produtos e pago R${valor_pago:.2f}. '
        f'Assim, o troco será de R${troco:.2f}')




