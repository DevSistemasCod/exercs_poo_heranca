class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    #Getters
    @property
    def nome(self): 
        return self._nome

    @property
    def idade(self): 
        return self._idade

    #Setters
    @nome.setter
    def nome(self, nome): 
        self._nome = nome

    @idade.setter
    def idade(self, idade): 
        self._idade = idade

    def mostra_dados(self):
        print(f"Nome: {self._nome}, Idade: {self._idade}")
    
    def __str__(self):
        return f"Nome: {self._nome}, Idade: {self._idade}"
    