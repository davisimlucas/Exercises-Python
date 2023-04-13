'''
Fazer um programa para ler o valor "r" do raio de um círculo, e depois mostrar o valor da área do
círculo com três casas decimais. A fórmula da área do círculo é a seguinte: 𝑎𝑟𝑒𝑎 = 𝜋. 𝑟^2.
Você pode usar o valor de 𝜋 fornecido pela biblioteca da sua linguagem de programação, ou então, se preferir, use
diretamente o valor 3.14159.
'''
import math
raio: float; area: float; perimetro: float; diam: float
raio = float(input('Digite um valor para o raio da circunferência: '))

diam = 2 * raio
perimetro = math.pi * diam
area = math.pi * (raio ** 2.0)

print(f'O valor do raio é de {raio:.1f}m, o perimetro é de {perimetro:.1f}m e a área é de {area:.2f} m^2')
