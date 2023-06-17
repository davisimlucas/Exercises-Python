# Exercícios FUNCTIONS:

## ex 01 (dataExtenso):
Exercício que o usuário entra com o dia, mês e ano e esses dados são armazenados em forma de array (list).
Essa lista é armazenada como variável e escrita junta pelo método join(), e como são dados inteiros, se utiliza o método. 
map()
<ul>
<li>Método "".join(): método usado para unir elementos de uma lista através de um separador, separador esse colocado antes ""</li>

```python
arr = ['olá,', 'como', 'vai?']
frase = " ".join(arr)
print(frase)
# saída = olá, como vai?
```
<li>Método map(): método que realiza uma determinada função em todos os elementos de uma lista (array) ===> map(function, list)</li>

```python
def double(number):
    return number * 2
number = [1, 2, 3]
doubleNumber = map(double, number)
```
</ul>
Para escrever a data em extenso, é necessário trancrever o mês. Para isso foi realizada uma função que associa o número do mês com seu nome, através de um dictionary e utiizando da função get().
Após, a data inserida é imprimida por extenso após um tempo de 3s (utilizando a library time)


