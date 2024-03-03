from pessoa import Pessoa
from aluno import Aluno

if __name__ == "__main__":
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    matricula = input("Digite a matrícula do aluno: ")
    curso = input("Digite o nome do curso que o aluno está cursando: ")
        
    aluno = Aluno(nome, idade, matricula, curso)
    aluno.mostra_dados()
    
