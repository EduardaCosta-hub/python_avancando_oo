from Midias_audiovisuais import Midias_audiovisuais
class Filme(Midias_audiovisuais):
    def __init__(self, pTitulo, pAno, pRoteirista, pDiretor, pGenero, pDuracao):
        super().__init__(pTitulo, pAno, pRoteirista, pDiretor, pGenero)
        self.__duracao = pDuracao
    
    #methods
    def mostra_informacoes(self):
        super().mostra_informacoes()
        print(f"Duração: {self.__duracao}")
    
    #properties
    @property
    def duracao(self):
        return self.__duracao
    @duracao.setter
    def duracao(self, pDuracao):
        self.__duracao = pDuracao