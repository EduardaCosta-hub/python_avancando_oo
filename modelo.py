class Filme:
    def __init__(self, pTitulo, pAno, pDuracao, pDiretor, pGenero):
        self.__titulo = pTitulo
        self.__ano = pAno
        self.__duracao = pDuracao
        self.__diretor = pDiretor
        self.__genero = pGenero
        self.__likes = 0
    
    #methods
    def dar_like(self):
        self.__likes += 1
        
    #properties
    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, pTitulo):
        self.__titulo = pTitulo
        
    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, pAno):
        self.__ano = pAno
        
    @property
    def duracao(self):
        return self.__duracao
    @duracao.setter
    def duracao(self, pDuracao):
        self.__duracao = pDuracao
    
    @property
    def diretor(self):
        return self.__diretor
    @diretor.setter
    def diretor(self, pDiretor):
        self.__diretor = pDiretor
    
    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def genero(self, pGenero):
        self.__genero = pGenero
    
    @property
    def likes(self):
        return self.__likes
    @likes.setter
    def titulo(self, likes):
        likes = self.__likes
        self.__likes = likes
        print("Você não pode alterar o número de likes manualmente. É necessário invocar o método 'dar_like()'")