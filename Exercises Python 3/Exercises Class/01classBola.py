class bola:
   
    def __init__(self, color, circ, material):
        self.color = color
        self.circ = circ
        self.material = material 

    def changeColor(self, newColor):
        self.color = newColor
    
    def showUpColor(self):
        print(f'A cor da bola é {self.color}')

