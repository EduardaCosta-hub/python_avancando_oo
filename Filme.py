from Midias_audiovisuais import Midias_audiovisuais
class Filme(Midias_audiovisuais):
    def __init__(self, pTitulo, pAno, pRoteirista, pDiretor, pGenero, pDuracao):
        super().__init__(pTitulo, pAno, pRoteirista, pDiretor, pGenero)
        self.__duracao = pDuracao
    @property
    def duracao(self):
        return self.__duracao
    @duracao.setter
    def duracao(self, pDuracao):
        self.__duracao = pDuracao