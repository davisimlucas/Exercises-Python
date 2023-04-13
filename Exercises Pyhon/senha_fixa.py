'''
Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
encerrado. Considere que a senha correta é o valor 2002.
'''
nome = str(input('Digite um nome para seu Login: '))
senha_correta = int(input('Crie um valor para sua senha: '))
senha = int(input('Digite o valor para senha: '))
if nome[-1] == 'a' or 'e':   #nome[-1] último elemento
    sufixo = str('a')
else:
    sufixo = str('o')
while senha != senha_correta:
    print('Senha incorreta!')
    print(f'Você não é {sufixo} {nome}?')
    senha = int(input('Tente novamente: '))
print(f'---------------------------\nSenha correta.\nBem vindo, {nome}.')

