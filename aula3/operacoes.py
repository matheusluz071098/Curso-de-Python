nome = input('digite seu nome: ')
sobrenome = input ('digete seu sobrenome: ')
print (nome + sobrenome)
idade = input('digite sua idade: ')
print(f'\n nome: {nome} \n  sobrenome: {sobrenome}\n  idade: {idade}')
if idade < '18':
    print('nao pode usar mecado tech, para o que presta')
if idade > '18':
    print ('beba com moderacao') 
else:
    print('ta comecando agora, va devagar')
