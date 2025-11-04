class Aula:
    def __init__(self, nome, horario, curso, professor):
        self.next = None
        self.prev = None
        self.nome = nome
        self.horario = horario
        self.curso = curso
        self.professor = professor


class ListaAulas:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, nome, horario, curso, professor):
        curr = self.head
        aula = Aula(nome, horario, curso, professor)
        if self.head is None:
            self.head = aula
            self.tail = aula
        elif curso < self.head.curso:
            self.head.prev = aula
            aula.next = self.head
            self.head = aula
        elif curso > self.tail.curso:
            self.tail.next = aula
            aula.prev = self.tail
            self.tail = aula
        else:
            while curr.curso < curso:
                curr = curr.next
            if curr.curso != curso:
                aula.next = curr
                aula.prev = curr.prev
                curr.prev.next = aula
                curr.prev = aula
    def print(self):
        curr = self.head
        print("Aulas:")
        while curr is not None:
            print("Nome: ", curr.nome)
            print("Horário: ", curr.horario)
            print("Curso: ", curr.curso)
            print("Professor: ", curr.professor)
            curr = curr.next
    def remove(self, nome):
        curr = self.head
        if self.head == None:
            return "Lista Vazia"
        else:
            while curr.nome != nome:
                curr = curr.next
            print("", curr.nome)
            
            if curr == self.head:
                self.head = curr.next
                curr.next.prev = None
            elif curr == self.tail:
                self.tail = curr.prev
                curr.prev.next = None
            else:
                if curr.next is not None:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
    def search(self, nome, curso):
        curr = self.head
        while curr.nome != nome:
            if(curr == self.tail and curr.nome != nome and curr.curso != curso):
                return "Aula não encontrada"
            curr = curr.next
        print("Aula encontrada:\n")
        print("Nome:", curr.nome)
        print("Curso:", curr.curso)
        print("Horário:", curr.horario)
        print("Professor: ", curr.professor)
        