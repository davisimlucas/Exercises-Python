# Exercícios FUNCTIONS:

### ex 01 (dataExtenso):
Exercício que o usuário entra com o dia, mês e ano e esses dados são armazenados em forma de array (list).
Essa lista é armazenada como variável e escrita junta pelo método join(), e como são dados inteiros, se utiliza o método. 
map()
<ul>
<li>Método "".join(): método usado para unir elementos de uma lista através de um separador, separador esse colocado antes ""</li>

```python
# método join()
arr = ['olá,', 'como', 'vai?']
frase = " ".join(arr)
print(frase)
# saída = olá, como vai?
```
<li>Método map(): método que realiza uma determinada função em todos os elementos de uma lista (array) ===> map(function, list)</li>

```python
# método map()
def double(number):
    return number * 2
number = [1, 2, 3]
doubleNumber = map(double, number)
print(doubleNumber) = [2, 4, 6]
```
</ul>
Para escrever a data em extenso, é necessário trancrever o mês. Para isso foi realizada uma função que associa o número do mês com seu nome, através de um dictionary e utiizando da função get().
Após, a data inserida é imprimida por extenso após um tempo de 3s (utilizando a library time)

### ex 03 (número reverso)
Exercício que retorna o número invertido.
Usuário entra com um número inteiro (str) e é definida uma função reverseNumber que recolhe a variável (number) e aloca em uma array com cada número sendo um elemento indexado, através da função list() e do método main() que aplica a função int() para todos os elementos do número str inserido. 
Após, a função realiza a função reverse() na lista formada, retornando o número inverso
```python 
# função reverse() para list ou array
arr = [1, 2, 3]
reverseArr = arr.reverse()
print(reverseArr)
#saída = [3, 2, 1]
```
