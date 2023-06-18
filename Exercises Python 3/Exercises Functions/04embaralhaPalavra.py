# Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
import random

def embaralhaTipo1(word):

    wordArray = list(map(str, word))
    size = len(wordArray)

    for i in range(size - 1, 0, -1):
        j = random.randint(0, i)
        wordArray[i], wordArray[j] = wordArray[j], wordArray[i]

    return ''.join(wordArray)

def embaralhaTipo2(word):

    wordArray = list(map(str, word))
    random.shuffle(wordArray)

    return ''.join(wordArray)

palavra = "python"
palavraEmbaralhada = print(embaralhaTipo2(palavra))
