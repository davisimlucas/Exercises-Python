'''
Uma empresa vai conceder um aumento percentual de
salário aos seus funcionários dependendo de quanto
cada pessoa ganha, conforme tabela ao lado. Fazer um
programa para ler o salário de uma pessoa, daí mostrar
qual o novo salário desta pessoa depois do aumento,
quanto foi o aumento e qual foi a porcentagem de
aumento.
até R$1000,00 => 20%
de R$1000,00 até R$3000,00 => 15%
de R$3000,00 até R$8000,00 => 10%
acima R$8000,00 => 5%
'''
salario: float; salario_novo: float; aumento: float; porcent: str
salario = float(input('Digite o valor do salário do funcionário: '))
if salario <= 1000:
    salario_novo = salario * 1.20
    aumento = salario_novo - salario
    porcent = str('20%')
elif 1000 < salario <= 3000:
    salario_novo = salario * 1.15
    aumento = salario_novo - salario
    porcent = str('15%')
elif 3000 < salario <= 5000:
    salario_novo = salario * 1.10
    aumento = salario_novo - salario
    porcent = str('10%')
else:
    salario_novo = salario * 1.05
    aumento = salario_novo - salario
    porcent = str('5%')
print(f'O salário do funcionário é de R${salario:.2f} \nO salário atulizado é de R${salario_novo:.2f}\n'
      f'O aumento foi de R${aumento:.2f} \nO aumento percentual de {porcent}')
