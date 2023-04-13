'''
Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C
'''
A = float(input('Digite um valor para medida A: '))
B = float(input('Digite um valor para medida B: '))
C = float(input('Digite um valor para medida C: '))

# a)
area_quadrado = A ** 2.0
# b)
area_triang = (A*B)/2.0
# c)
area_trap = ((A*B)*C)/2.0

print(f'As areas do quadrado, triãngulo retângulo e do trapézio são, respectivamente:'
      f' {area_quadrado:.1f}, {area_triang:.1f} e {area_trap:.1f}')