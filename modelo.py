class Usuario:
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._senha = senha
        self._email = email
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        
    @property
    def senha(self):
        return self._senha
        
    @property
    def email(self):
        return self._email

class Programa:
    def __init__(self, nome, generos, ano):
        self._nome = nome
        self.generos = generos
        self.ano = ano
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
class Filme(Programa):
    def __init__(self, nome, generos, ano, duracao):
        super().__init__(nome, generos, ano)
        self.duracao = duracao
    
class Serie(Programa):
    def __init__(self, nome, generos, ano, temporadas):
        super().__init__(nome, generos, ano)
        self.temporadas = temporadas

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        
    def __getitem__(self, item):
        return self._programas[item]
        
    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)

