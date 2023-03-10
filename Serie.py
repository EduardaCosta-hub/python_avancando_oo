from Midias_audiovisuais import Midias_audiovisuais
class Serie(Midias_audiovisuais):
    def __init__(self, pTitulo, pAno, pRoteirista, pDiretor, pGenero, pTemporadas):
        super().__init__(pTitulo, pAno, pRoteirista, pDiretor, pGenero)
        self.__temporadas = pTemporadas
        
    #methods
    def __str__(self):
        super().mostra_informacoes()
        return f"Temporadas: {self.__temporadas}"
    
    #properties
    @property
    def temporada(self):
        return self.__temporadas
    @temporada.setter
    def temporada(self, pTemporadas):
        self.__temporadas = pTemporadas 