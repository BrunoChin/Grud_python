class Usuario:
    def __init__(self, nome, email, idade):
        self.__nome = nome
        self.__email = email
        self.__idade = idade
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    
usuario1 = Usuario("Bruno", "Bruno@gmail.com", 22)

