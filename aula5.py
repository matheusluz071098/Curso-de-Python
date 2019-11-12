# Crie um programa que leia 4 notas
# imprima a maior nota
#imprima a menor nota
# imprima a media
#imprima se o aluno foi aprovado ou reprovado 

var

n1= float (input ('digite sua nota : '))
n2= float (input ('digite sua segunda nota : '))
n3= float (input ('digite sua terceira nota : '))
n4= float (input ('digite sua quarta nota : '))

media= ((n1+n2+n3+n4)/4)




if n1 > n2 and n1 > n3 and n1 > n4: 
    
    print ('maior nota n1')
    
elif n2 > n1 and n2 > n3 and n2 > n4:
    print('maior nota n2')

elif n3 > n2 and n3 > n1 and n3 > n4:
    print ('maior nota n3')

elif n4 > n3 and n4 > n2 and n4 > n1:
    print('maior nota n4')



if n1 < n2 and n1 < n3 and n1 < n4: 
    
    print ('menor nota n1')
    
elif n2 < n1 and n2 < n3 and n2 < n4:
    print('menor nota n2')

elif n3 < n2 and n3 < n1 and n3 < n4:
    print ('menor nota n3')

elif n4 < n3 and n4 < n2 and n4 < n1:
    print('menor nota n4')

if media >= 7 :
    print ('aprovado')

elif media < 7 :
    print ('reprovado')

