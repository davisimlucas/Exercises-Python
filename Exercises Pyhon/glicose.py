'''
Fazer um programa para ler a quantidade de glicose
no sangue de uma pessoa e depois mostrar na tela a
classificação desta glicose de acordo com a tabela de
referência ao lado.
normal: até 100 mg/dl
elevado: entre 100 e 140 mg/dl
diabetes: maior que 140 mg/dl
'''

glicose = float(input('Digite um valor para glicose do paciente: '))

if glicose <= 100:
    print('Glicose normal.')
elif 100 < glicose <= 140:
    print('Glicose elevada.')
elif 140 < glicose <= 170:
    print('Diabetes, procure um médico para tratamento!')
else:
    print('Diabetes avançada, recomende a sua família a procurar o tamanho certo de seu caixão.')

