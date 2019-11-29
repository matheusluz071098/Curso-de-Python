# Aula 16 - 29-11-2019
# ??????????

from faixa import criar_faixa,salvar_faixa,ler_faixa


# Cadastro de playlist
# lendo musica, artista e album

musica = input('digite sua musica: ')
artista = input('digite sua artista: ')
album = input('digite sua album: ')

mus= criar_faixa(musica, artista, album)
salvar_faixa(mus)
lista= ler_faixa()

for faixa in lista:
    print(f'{faixa["musica"]} - {faixa["artista"]} - {faixa["album"]}')