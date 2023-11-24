class Aluno:
    def __init__(self):
        self.nome=""
        self.email=""
        self.nota1=0
        self.nota2=0
      
    def imprimirinformacoes(self):
        self.media = self.calcularMedia()
        
        print(f"""Nome: {self.nome})
                  E-mail:{self.email}
                  Nota 1:{self.nota1}
                  Nota 2:{self.nota2}
                  Media: {self.media}
                  resultado:{self.informarSituacao(self.media )}""")
        
    def calcularMedia(self):
        return (self.nota1+self.nota2)/2
    
    def informarSituacao(self, m):
        if m >= 7:
            return "Aprovado"
        else:
            return "Reprovado" 
                   
        
class Curso:
    def __init__(self,c,v):
        self.name = c
        self.valor= v
        
def listar(self.Aluno):
    for elemento in self.Aluno:
        print(f"""Nome: {self.nome})
                  E-mail:{self.email}
                  Nota 1:{self.nota1}
                  Nota 2:{self.nota2}
                  Media: {self.media}
                  resultado:{self.informarSituacao(self.media )}""") 
        
        
           
    