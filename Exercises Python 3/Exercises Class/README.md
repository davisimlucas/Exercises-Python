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

## Ex 04 (class pessoa)
Novamente se usa o método init para criar os atributos dos valores que serão referência nos métodos.
Determinando os atributos, foram criadas as funções que realizariam os métodos através do self, referenciando os atributos anteriores. 
Destaque para função envelhecer que caso a pessoa tenha menos que 21 anos, a cada ano que ela envelhece, sua altura aumenta 0,5 * número de anos, assim, se cria um parâmetro "ano" que interage com os parâmetros do método init, referenciados somente pelo self.

```python
#exemplo
class exemple:
    def __init__(self, a):
        self.a = a

    def function(self, b)
    return self.a * b
```
