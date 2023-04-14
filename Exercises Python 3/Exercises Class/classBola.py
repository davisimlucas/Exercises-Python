class bola:
    '''
    método init ===> construtor da class, serve para inicializar os atributos do objetc com valores padrão ou com 
    valores fornecidos pelo usuário no momento de criação do object.
    '''
    def __init__(self, color, circ, material):
        self.color = color
        self.circ = circ
        self.material = material 

    def changeColor(self, newColor):
        self.color = newColor
    
    def showUpColor(self):
        print(f'A cor da bola é {self.color}')

