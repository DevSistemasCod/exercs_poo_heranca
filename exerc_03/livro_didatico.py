from livro import Livro

class LivroDidatico(Livro):
    def __init__(self, titulo, autor, num_paginas, disciplina, ano_escolar, nivel_ensino):
        super().__init__(titulo, autor, num_paginas)
        self.__disciplina = disciplina
        self.__ano_escolar = ano_escolar
        self.__nivel_ensino = nivel_ensino

    #Getters
    @property
    def disciplina(self):
        return self.__disciplina
    
    @property
    def ano_escolar(self):
        return self.__ano_escolar
    
    @property
    def nivel_ensino(self):
        return  self.__nivel_ensino

    #Setters
    @disciplina.setter
    def disciplina(self, disciplina):
        self.__disciplina = disciplina
    
    @ano_escolar.setter
    def ano_escolar(self, ano_escolar):
        self.__ano_escolar = ano_escolar
    
    @nivel_ensino.setter
    def nivel_ensino(self, nivel_ensino):
        self.__nivel_ensino = nivel_ensino

    def informar_detalhes(self):
        super().informar_detalhes()
        print(f"Disciplina: {self.__disciplina}")
        print(f"Ano Escolar: {self.__ano_escolar}")
        print(f"Nível de Ensino: {self.__nivel_ensino}")
