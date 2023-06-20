# Crie uma classe que modele um quadrado:
#   Atributos: Tamanho do lado
#   Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área

class quadrado:
    def __init__(self, lado):
        self.lado = lado

    def ladoChange(self, lado):
        self.lado = lado 
    
    def printLado(self):
        return self.lado
       
    def area(self):
        return self.lado ** 2

quad = quadrado(5)
print(quad.printLado())
quad.ladoChange(9)
print(quad.printLado())
print(quad.area())
