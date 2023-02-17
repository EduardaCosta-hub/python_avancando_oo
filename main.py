from Filme import Filme
from Serie import Serie
filme1 = Filme("Titulo generico",2023,"Fulano","Siclano","Comédia Romantica",100)
serie1 = Serie("Uma série",2023,"Roteiro","Direção","Comédia",4)
midias = {filme1, serie1}
for conteudo in midias:
    conteudo.mostra_informacoes()
    print("")