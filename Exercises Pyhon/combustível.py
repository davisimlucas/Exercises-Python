'''
Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma:
1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a
4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o
código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem
como as quantidades de cada combustível.
'''
codigo = int(input('Digite um valor para o código: '))
alcool = int(0)
gasolina = int(0)
diesel = int(0)
while codigo != 4:
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
    codigo = int(input('Digite outro valor para o código: '))
print(f'Muito Obrigado pela colaborção. \nÁlcool = {alcool}\nGasolina = {gasolina}\nDiesel = {diesel}')


