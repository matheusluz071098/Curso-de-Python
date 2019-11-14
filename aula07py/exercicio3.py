#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)


listanotas = []
somanotas = 0
listaaprovacao = []

for i in range(0,2):
    aluno = input("Qual nome do aluno: ")
    somanotas = 0

    for j in range(4):
        nota = float(input(f'Qual a nota número {j+1} de {aluno}: '))
        somanotas += nota 
    calculonotas = somanotas / 4
    listanotas.append(calculonotas)
    if  calculonotas >= 7 :
        listaaprovacao.append(f'{aluno} - Média: {calculonotas} - aprovado')
    else:
        listaaprovacao.append(f'{aluno} - Média: {calculonotas} - reprovado')

for i in listaaprovacao:
    print(i)

    





