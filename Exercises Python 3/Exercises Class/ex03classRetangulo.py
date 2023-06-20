'''Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, 
deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.'''

class retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLado(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB 

    def retornarLados(self):
        return self.ladoA
        return self.ladoB

    def area(self):
        return self.ladoA * self.ladoB

    def perimetro(self):
        return 2 * self.ladoA + 2 * self.ladoB

# pisos:
ladoA = float(input('Informe a medida do lado A: '))
ladoB = float(input('Informe a medida do lado B: '))

Retangulo = retangulo(ladoA, ladoB)

areaRetangulo = Retangulo.area()
perimetroRetangulo = Retangulo.perimetro()

piso = float(input('Informe a medida do piso: '))
rodape = float(input('Informe a altura do rodapé: '))

areaPiso = piso ** 2
areaRodape = piso * rodape

n_pisos = areaRetangulo / areaPiso
n_rodapes = perimetroRetangulo * rodape

print(f'Quantidade de pisos necessário é: {n_pisos}\
    Quantidade de rodapés necessários: {n_rodapes}')
 
