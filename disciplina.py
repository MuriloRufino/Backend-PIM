#essa classe é pra tabela de notas do front
class Disciplina:
    def __init__(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = (nota1 + nota2 + nota3)/3

class ListaDisciplinas:
    def __init__(self):
        self.head = None
        self.tail = None