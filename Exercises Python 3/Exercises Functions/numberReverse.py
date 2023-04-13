# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverseNumber(variable):
    numberList = list(map(int, str(variable)))
    numberList.reverse()
    return ''.join(map(str, numberList))

number = input('Enter a number: ')
reversedNumber = reverseNumber(number)
print(reversedNumber)
