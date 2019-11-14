# exercicio 1 - dicionario
# # escreva programa que leia os dados de cerveja
# cerveja: marca, tipo, ibu, abv, ebc, volume
# crie um dicionario para armazenar os dados
# imprima os dados do dicionario (não dicionario completo)


cerveja= input ('Digite o nome da sua cerveja: ')
tipo= input ('Digite o tipo da sua cerveja: ')
ibu= input ('ibu:  ')
abv=  input ('abv: ')
ebc= input ('ebc: ')
volume = input ('volume: ')


dicionario_nome = {'cerveja':cerveja, 'tipo': tipo,'ibu':ibu,'abv':abv,'ebc':ebc, 'volume':volume}
print(f"{dicionario_nome['cerveja']} | {dicionario_nome['tipo']} | {dicionario_nome['ibu']} | {dicionario_nome['abv']} | {dicionario_nome['ebc']} | {dicionario_nome ['volume']}")
