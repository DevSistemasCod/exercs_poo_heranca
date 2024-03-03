from livro import Livro

class LivroDeFiccao(Livro):
    def __init__(self, titulo, autor, num_paginas, genero, subgenero):
        super().__init__(titulo, autor, num_paginas)
        self.__genero = genero
        self.__subgenero = subgenero

    # Getters
    @property
    def genero(self):
        return self.__genero

    @property
    def subgenero(self):
        return self.__subgenero

    # Setters
    @genero.setter
    def genero(self, genero):
        self.__genero = genero

    @subgenero.setter
    def subgenero(self, subgenero):
        self.__subgenero = subgenero

    # Demais Métodos
    def sinopse_do_livro(self):
        print(f"Sinopse: Este livro de {self.__genero} aborda a história no subgênero {self.__subgenero}.")

    def informar_detalhes(self):
        super().informar_detalhes()
        print(f"Gênero: {self.__genero}")
        print(f"Subgênero: {self.__subgenero}")
