class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco

    @property
    def telefone(self):
        return self._telefone

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
