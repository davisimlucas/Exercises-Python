# jogo de craps
import random

def gameCraps():
    while True:
        ask = str(input('Você deseja jogar os dados? (s/n)\n'))

        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        result = (dado1 + dado2)
        print(f'Os números dos dados foram: {dado1} e {dado2}\n\
        Assim, sua pontuação é {result}')

        if result == 7 or result == 11:
            print('Você é um "natural". Você ganhou!')
            break
        elif result == 2 or result == 3 or result == 12:
            print('Você tirou um "craps"! Você perdeu!')
            break
        else:
            ponto = result
            print(f'{result} é seu Ponto.')
            while True:
                ask = str(input('Você deseja jogar os dados? (s/n)\n'))
                if ask == 's':
                    dado1 = random.randint(1, 6)
                    dado2 = random.randint(1, 6)
                    result = (dado1 + dado2) 
                    print(f'Os números dos dados foram: {dado1} e {dado2}\nAssim, sua pontuação é {result}')   
                    if result == ponto:
                        print('Você ganhou!')
                        return
                    elif result == 7:
                        print('Você perdeu!')
                        return
                else:
                    return
    
gameCraps()

        

        


        
        
