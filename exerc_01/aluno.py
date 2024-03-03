from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.__matricula = matricula
        self.__curso = curso

    #Getters
    @property
    def matricula(self): 
        return self.__matricula

    @property
    def curso(self): 
        return self.__curso

    #Setters
    @matricula.setter
    def matricula(self, matricula): 
        self.__matricula = matricula

    @curso.setter
    def curso(self, curso): 
        self.__curso = curso

    def mostra_dados(self):
        super().mostra_dados()
        print(f"Matrícula: {self.__matricula}, Curso: {self.__curso}")