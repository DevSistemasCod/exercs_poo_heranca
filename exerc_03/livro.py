class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self._titulo = titulo
        self._autor = autor
        self._num_paginas = num_paginas

    #Getters
    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def num_paginas(self):
        return self._num_paginas

    #Setters
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @num_paginas.setter
    def num_paginas(self, num_paginas):
        self._num_paginas = num_paginas

    # Demais Métodos
    def informar_detalhes(self):
        print(f"Título: {self._titulo}")
        print(f"Autor: {self._autor}")
        print(f"Número de Páginas: {self._num_paginas}")
