import math
a: float; b: float; c: float
delta: float; x1: float; x2: float
a = float(input('Coeficiente a: '))
b = float(input('Coeficiente b: '))
c = float(input('Coeficiente c: '))
delta = (b ** 2.0) - (4 * a * c)   #potenciação em pyton: x ** y: x elevado a y
if delta < 0:
    print('Não possui raízes reais')
else:
    x1 = ((-b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-b) - math.sqrt(delta)) / (2 * a)
    print(f'x1 = {x1:.2f}')
    print(f'x2 = {x2:.2f}')
print('y = ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c))