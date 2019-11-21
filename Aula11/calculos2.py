from metodos2 import *

valor = float(input('Digite o valor do investimento: '))
anos = float(input('Digite a quantidade de anos a ser caculado o lucro do investimento: '))

for i in range(int(anos+1)):
    meses = i*12

print('rentabilidade %0.2f' %CalculoInvestimento(valor,meses))
