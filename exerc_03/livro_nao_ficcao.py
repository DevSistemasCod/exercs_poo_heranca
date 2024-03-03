from livro import Livro

class LivroDeNaoFiccao(Livro):
    def __init__(self, titulo, autor, num_paginas, tema, topico):
        super().__init__(titulo, autor, num_paginas)
        self.__tema = tema
        self.__topico = topico

    # Getters
    @property
    def tema(self):
        return self.__tema
    
    @property
    def topico(self):
        return self.__topico

    # Setters
    def tema(self, tema):
        self.__tema = tema
    
    def topico(self, topico):
        self.__topico = topico

    # Demais Métodos
    def recomendar_outros_titulos(self):
        print(f"Recomendação: Confira outros títulos relacionados ao tema {self.__tema} e tópico {self.__topico}.")

    def informar_detalhes(self):
        super().informar_detalhes()
        print(f"Tema: {self.__tema}")
        print(f"Tópico: {self.__topico}")
