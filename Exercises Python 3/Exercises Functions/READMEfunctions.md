# Exercícios FUNCTIONS:

## ex 01 (dataExtenso):
exercício que o usuário entra com o dia, mês e ano e esses dados são armazenados em forma de array (list)
essa lista é armazenada como variável e escrita junta pelo método join(), e como são dados inteiros, se utiliza o método 
map()
<ul>
    <li>método "".join(): método usado para unir elementos de uma lista através de um separador, separador esse colocado antes ""</li>

    ```python
    arr = ['olá,', 'como', 'vai?']
    frase = " ".join(arr)
    ```
    <li>método map(): método que realiza uma determinada função em todos os elementos de uma lista (array) ===> map(function, list)</li>

    ```python
    def double(number):
        return number * 2
    number = [1, 2, 3]
    doubleNumber = map(double, number)
    ```
</ul>


