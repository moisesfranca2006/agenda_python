from modelos import Aluno, Curso, listar

estudante=Aluno()
estudante.nome="Juan"
estudante.email="juan@gmail.com"
estudante.nota1=8.0
estudante.nota2=6.5
estudante.endereco="Rua 10"

print(estudante.nome)
print(estudante.endereco)
print(estudante.imprimirinformacoes())

estudante2=Aluno()
estudante2.nome="Pedro"
estudante2.email="pedro@gmail.com"
estudante2.nota1=10.0
estudante2.nota2=8.0
print(estudante2.imprimirinformacoes())

estudante3=Aluno()
print(estudante3.nome)

cursoWord= Curso("word", 100)
print(estudante3.imprimirinformacoes())

listar(Aluno)
