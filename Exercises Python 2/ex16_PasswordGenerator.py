'''
Write a password generator in Python. Be creative with how you generate passwords 
- strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
Concepts: 
Python's random module
'''
import random

def passwordGenerator():
    alfabeto_m = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 's', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
    alfabeto_M = [letra.upper() for letra in alfabeto_m]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    caracteres = ['!','@', '$', '%', '&', '*', '+', '_']

    while True:
        type_of_Password = str(input('Senha forte ou fraca? ')).lower()
        password = []

        if type_of_Password == 'fraca':
            for valorEasy in range(1, random.randint(4, 6)):
                valorEasy = random.choice(alfabeto_m) or random.choice(numbers)
                password.append(valorEasy)
            password[0] = random.choice(alfabeto_M) + password[0] 
        elif type_of_Password == 'forte':
            for valorStrong in range(1, random.randint(10, 12)):
                valorStrong = random.choice(alfabeto_m) or random.choice(numbers) or ramdom.choice(caracteres)
                password.append(valorStrong)
            password[0] = random.choice(alfabeto_M) + password[0]   
            password[-1] = password[-1] + random.choice(caracteres) 
            password[-2] = password[-2] + random.choice(numbers)
            password[-3] = password[-3] + random.choice(numbers)
        
        else:
            print('Digite para essa questão "fraco" ou "forte".') 
            continue
        print(F'A senha gerada é: {"".join(map(str, password))}\n')
        question = str(input('Deseja criar uma nova senha? (s/n) ')).lower()
        
        if question == 's':
            continue
        else: 
            print(f'Sua senha continua sendo {"".join(map(str, password))}\n')    
            break
passwordGenerator()