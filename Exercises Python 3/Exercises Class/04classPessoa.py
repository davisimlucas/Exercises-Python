'''Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome 
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def crescer(self, cent):
        self.altura += cent
    
    def envelhercer(self, ano):
        self.idade += ano
        if self.idade < 21:
            self.altura = self.altura + ano / 2

    def emagrecer(self, quilos):
        self.peso -= quilos

    def engordar(self, quilos):
        self.peso += quilos

#exemplo de programa pra usar:
pessoa1 = pessoa("Davi", 15, 70, 174)

pessoa1.crescer(3)
print(pessoa1.altura) # 177

pessoa1.envelhercer(4)
print(f'{pessoa1.idade}, {pessoa1.altura}') # 29, 179 (177 + 4 anos * 0,5)

pessoa1.emagrecer(2)
print(pessoa1.peso) # 68

pessoa1.engordar(7)
print(pessoa1.peso) # 75 (68+7)
