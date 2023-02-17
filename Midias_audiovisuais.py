class Midias_audiovisuais:
    def __init__(self, pTitulo, pAno, pRoteirista, pDiretor, pGenero):
        self.__titulo = pTitulo
        self.__ano = pAno
        self.__roteirista = pRoteirista
        self.__diretor = pDiretor
        self.__genero = pGenero
        self.__likes = 0
    
    #methods
    def dar_like(self):
        self.__likes += 1
        
    def mostra_informacoes(self):
        print(f"Título: {self.__titulo}")
        print(f"Ano: {self.__ano}")
        print(f"Roteirista: {self.__roteirista}")
        print(f"Diretor: {self.__diretor}")
        print(f"Gênero: {self.__genero}")
        print(f"Likes: {self.__likes}")
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
    def roteirista(self):
        return self.__roteirista
    @roteirista.setter
    def roteirista(self, pRoteirista):
        self.__roteirista = pRoteirista
    
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
    def likes(self, likes):
        likes = self.__likes
        self.__likes = likes
        print("Você não pode alterar o número de likes manualmente. É necessário invocar o método 'dar_like()'")