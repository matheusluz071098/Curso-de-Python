#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)


aluno = []
notas = []

for i range (1,11):
    aluno.append(input ('aluno:'))
    for i range (0,4):
         notas.append(input ('notas:'))

