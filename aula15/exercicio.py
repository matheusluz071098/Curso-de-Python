def salvar_cerveja(pessoa_dicionario):
    arquivo= open('cervejas.txt','a')
    arquivo.write(f"{pessoa_dicionario['nome_da_bebida']};{pessoa_dicionario['tipo_da_bebida']};{pessoa_dicionario['teor']}\n")
    arquivo.close()

def ler():
    lista= []
    arquivo= open('cervejas.txt','r')
    for linha in arquivo:
        linha= linha.strip()
        lista_linha= linha.split(";")
        cerveja= {'nome da bebida':lista_linha[0],'tipo da bebida':lista_linha[1],'teor':lista_linha[2]}
        lista.append(cerveja)
    arquivo.close()
    return lista

def inputo():

    nome_da_bebida = input('digite sua bebida: ')
    tipo_da_bebida = input('digite o tipo da bebida: ')
    teor= input('digite o teor alcoolico: ')
    cerveja={'nome_da_bebida':nome_da_bebida,'tipo_da_bebida':tipo_da_bebida,'teor':teor}
    return cerveja
salvar_cerveja(inputo())


lista = ler()
for p in lista:
    print(f"{p['nome da bebida']} - {p['tipo da bebida']} - {p['teor']}")