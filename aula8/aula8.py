# aula 8 - 14/11/2019
# Dicionario 

lista = []
dicionario = {'nome':'matheus','sobrenome':'luz'}
print(dicionario)
print(dicionario['sobrenome'])

nome= 'matheus'
lista_notas=[10,20,50,70]
media = sum(lista_notas)/len(lista_notas)
situacao = 'reprovado'
if media >=7:
    situacao='aprovado'
dicionario_aluno = {'nome':nome, 'lista_notas': lista_notas,'media':media,'situacao':situacao}

print(f"{dicionario_aluno['nome']} - {dicionario_aluno['situacao']}")
