'''
 Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
duas casas decimais.
'''
area: float; preco: float
comprimento = float(input('Digite um valor do Comprimento do terreno: '))
largura = float(input('Digite um valor da largura do terreno: '))
valor = float(input('Digite um valor do valor do metro quadrado: '))

area = comprimento * largura
preco = area * valor

print(f'O valor da área do terreno é de {area:.1f} metros quadrados.')
print(f'O valor do terreno será de R${preco:.2f}')
