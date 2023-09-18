class Usuario:
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._senha = senha
        self._email = email
    
    def __str__(self):
        return f"Nome: {self._nome} - Email: {self._email}"
    
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
        
    def __str__(self):
        return f"Nome: {self._nome} - Generos: {self.generos} - Ano: {self.ano}."
    
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
    
    def __str__(self):
        return f"Nome: {self._nome} - Generos: {self.generos} - Ano: {self.ano} - {self.duracao} min."
    
class Serie(Programa):
    def __init__(self, nome, generos, ano, temporadas):
        super().__init__(nome, generos, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f"Nome: {self._nome} - Generos: {self.generos} - Ano: {self.ano} - {self.temporadas} temporadas."

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        
    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
        
    @property
    def listagem(self):
        return self._programas
    
filme1 = Filme("Homem-Aranha longe de casa", ["Ação", "Super herois"], 2020, 160)
filme2 = Filme("Senhor dos aneis: A Sociedade do anel ", ["Aventura"], 2001, 230)

serie1 = Serie("A roda do tempo", ["Aventura"], 2019, 2)

programas = [filme1, filme2, serie1]

playlist1 = Playlist("Fim de semana", programas)

for programa in playlist1:
    print(programa)

print(f"Tamanho: {len(playlist1)}")