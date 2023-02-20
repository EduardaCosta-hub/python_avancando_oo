from Filme import Filme
from Serie import Serie
from Playlist import Playlist
filme1 = Filme("Titulo generico",2023,"Fulano","Siclano","Comédia Romantica",100)
serie1 = Serie("Uma série",2023,"Roteiro","Direção","Comédia",4)
programas = [filme1, serie1]
playlist1 = Playlist("Playlist de Teste", programas)
print(f"Tamanho da Playlist: {len(playlist1)}")
for programa in playlist1:
    print(programa)
    print("")
