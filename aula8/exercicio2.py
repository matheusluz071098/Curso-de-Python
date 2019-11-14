# exercicio 2 - dicionario
# escreva um programa que leia os dados de 11 jogadores
# jogador: nome, posicao, numero, perna Boa
# crie um dicionario para armazenar os dados
# imprima todos os jogadores e seus dados


dic = ['nome','posicao','numero','perna_boa']
lista = []
for i in range(0,2):
    dic = {'nome':input("digite nome: "),'posicao':input('digite posicao '),'numero':input('digite numero '),'perna_boa':input('digite perna_boa ')}
    lista.append(dic)
for j in lista:
    print(j['nome'],j['posicao'],j['numero'],j['perna_boa'])
