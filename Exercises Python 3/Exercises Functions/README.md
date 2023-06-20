# Exercícios FUNCTIONS:

## Ex 01 (dataExtenso):
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
<li>Método map(): método que realiza uma determinada função em todos os elementos de uma lista (array) ===> map(function, list)
</li>

```python
# método map()
def double(number):
    return number * 2
number = [1, 2, 3]
doubleNumber = map(double, number)
print(doubleNumber) #= [2, 4, 6]
```
</ul>
Para escrever a data em extenso, é necessário trancrever o mês. Para isso foi realizada uma função que associa o número do mês com seu nome, através de um dictionary e utiizando da função get().
Após, a data inserida é imprimida por extenso após um tempo de 3s (utilizando a library time)

## Ex 02 (jogo de Craps)
Exercício para definir uma função que realiza o jogo de Craps.

<ul>
    <li>REGRAS DO JOGO:</li>
</ul>

O usuário sorteia dois números de 1 a 6. A soma desses dois números se for igual ou a 7 ou a 11, o usuário é uma "Natural". 
Se a soma for igual a 2, ou 3 ou 12, o usuário é um "Craps" e ele perde.
Caso não seja nenhum dos casos acima, a soma é seu "Ponto". O usuário poderá jogar novamente dois números aleatórios de 1 a 6 e se a soma deles for igual ao seu "Ponto", ele ganha; se for igual a 7, ele perde. Se for diferente, poderá continuar sortendo os valores até conseguir. 

<ul>
    <li>Lógica do programa:</li>
</ul>
A principal lógica da função se concentra nos dois while looping, um dentro de outro:

O primeiro é o da primeira jogada, que pergunta se o usuário deseja jogar e realiza o primeiro sorteio. Caso essa jogada seja definitiva, ele volta a pergunta se o usuário deseja jogar novamente, se for "n", o looping break.

O segundo é para caso o usuário possua um "Ponto", assim, todas as vezes que seu próximo sorteio for diferente de seu "Ponto" ou diferente de 7, o while recomeça e pergunta se ele deseja jogar de novo. Caso uma das duas opções ocorram, o looping break, e volta para o primeiro looping 

## Ex 03 (número reverso)
Exercício que retorna o número invertido.
Usuário entra com um número inteiro (str) e é definida uma função reverseNumber que recolhe a variável (number) e aloca em uma array com cada número sendo um elemento indexado. 

Através da função list() e do método main() que aplica a função int() para todos os elementos do número str inserido. 
Após, a função realiza a função reverse() na lista formada, retornando o número inverso
```python 
# função reverse() para list ou array
arr = [1, 2, 3]
reverseArr = arr.reverse()
print(reverseArr)
#saída = [3, 2, 1]
```

## Ex 04 (embaralha palavras)
<ul>
    <li>Primeiro modo: </li>
</ul>

No primeiro modelo é criada uma função que recebe como parâmetro uma string e aloca cada letra como um elemento de uma lista através do método list() e com o método map(), mantém os elementos como string. O tamanho da lista é determinado pela função len()
Assim, é criado um for looping que faz correr uma iteração i na sequência saindo do tamanho - 1(-1 pois index inicia em 0) e até o 0 em passo -1. Nisso é atribuída uma variável iterável j a um valor aleatório pela função randint() da library random entre zero e o valor do tamanho da list. 
Após há uma troca dos valores que se referem a list[i] e list [j] pela seguinte associação comum em Python:
```python
def(a, b)
    a, b = b, a
    # a passa valer o que vale b e b passa valer o que vale a
```
Assim, se garante que a nova palavra formada pelas iterações j sejam de elementos aleatórios e não repetidos.

<ul>
    <li>Segundo modo: </li>
</ul>

O segundo modo estabelece os mesmos parâmetros para a lista que o primeiro modo. Contudo é utilizada a função shuffle() da library random que realiza o embaralhamento automático dos elementos de uma lista.

```python
import random

a[1, 2, 3, 4]
emb = random.shuffle(a)
print(emb)
#saída: uma possível ==> [2, 4, 1, 3]
```



