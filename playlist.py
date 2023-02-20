class Playlist():
    def __init__(self, pNome, pProgramas):
        self.nome = pNome
        self.__programas = pProgramas
    
    def __getitem__(self, item):
        return self.__programas[item]
    
    def __len__(self):
        return len(self.__programas)