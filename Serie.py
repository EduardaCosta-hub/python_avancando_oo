from Midias_audiovisuais import Midias_audiovisuais
class Serie(Midias_audiovisuais):
    def __init__(self, pTitulo, pAno, pRoteirista, pDiretor, pGenero, pTemporadas):
        super().__init__(pTitulo, pAno, pRoteirista, pDiretor, pGenero)
        self.__temporadas = pTemporadas
        
    #methods
    def mostra_informacoes(self):
        super().mostra_informacoes()
        print(f"Duração: {self.__temporadas}")
    
    #properties
    @property
    def temporada(self):
        return self.__temporadas
    @temporada.setter
    def temporada(self, pTemporadas):
        self.__temporadas = pTemporadas 