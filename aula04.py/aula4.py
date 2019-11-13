#aula 4
# fazer um programa que leia 2 mumeros 
# realizar as 4 operacoes matematicas
# imprima o resultado das operacoes
# diga qual é o maior dos dois numeros

n1= int (input ('digite seu primeiro numero: '))
n2 = int( input ('digite seu segundo numero: '))
soma = n1 + n2
print(soma)
subtracao= n1 - n2
print(subtracao)
multiplicacao = n1 * n2
print(multiplicacao)
divisao = n1 / n2
print(divisao)

if n1 > n2:
    print ('n1 é maior que n2')

if n1 < n2:
 print('n2 e maior')

else: 
    print ('sao iguais')