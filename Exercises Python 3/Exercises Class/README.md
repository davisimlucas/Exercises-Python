# Exercícios CLASS:

## ex 01 (classBola)
método __init__ ===> construtor da class, serve para inicializar os atributos do objetc com valores padrão ou com valores fornecidos pelo usuário no momento de criação do object.
```python
class exemple:
    def __init__(self, obj):
        self.obj = obj
```
self é uma referência ao objeto atual em que o método está sendo chamado e é usado para acessar e manipular os atributos desse objeto.

## Ex 02 (class quadrado):
Novamente usa-se o método __init__ com o self para a construção dos parâmetros e através deles estabelecer os métodos baseados no parâmetro self da função do método __init__

## Ex 03 (class retangulo):
Novamente é criada uma classe utilizando o método __init__ juntamente com o self. para a atribuição dos valores ao objeto.
Com isso, realiza-se os métodos de cálculo de área e perímetro, e mudança dos valores dos lados utilizando o self. que mantém os lados como referenciados. 

Com isso, inicia-se o programa, pedindo ao usuário inserir dois valores de lados e, com eles, é criado um objeto "Retangulo" que é uma instância da classe "retangulo", possuindo todos os métodos já definidos pela classe.
