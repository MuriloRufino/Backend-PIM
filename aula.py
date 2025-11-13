class Aula:
    def __init__(self, nome, data ,inicio, fim, curso, professor, conteudo):
        self.next = None
        self.prev = None
        self.nome = nome
        self.data = data
        self.inicio = inicio
        self.fim = fim
        self.curso = curso
        self.professor = professor
        self.conteudo = conteudo
        
class ListaAulas:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, nome, data, inicio, fim, curso, professor, conteudo):
        curr = self.head
        aula = Aula(nome, data, inicio, fim, curso, professor, conteudo)
        if self.head is None:
            self.head = aula
            self.tail = aula
        elif nome <= self.head.nome and data <= self.head.data:
            self.head.prev = aula
            aula.next = self.head
            self.head = aula
        elif nome >= self.tail.nome:
            self.tail.next = aula
            aula.prev = self.tail
            self.tail = aula
        else:
            while curr.nome <= nome and data <= self.head.data:
                curr = curr.next
            if curr.nome != nome:
                aula.next = curr
                aula.prev = curr.prev
                curr.prev.next = aula
                curr.prev = aula
    def insert_obj(self, aula_obj):
        if self.head == None:
            self.head = aula_obj
            self.tail = aula_obj
        else:
            self.head.prev = aula_obj
            aula_obj.next = self.head
            self.head = aula_obj
    def print(self):
        curr = self.head
        print("Aulas:")
        while curr is not None:
            print("Nome: ", curr.nome)
            print("Data:", curr.data)
            print("Início: ", curr.inicio)
            print("Fim: ", curr.fim)
            print("Curso: ", curr.curso)
            print("Professor: ", curr.professor)
            curr = curr.next
    def remove(self, nome, data):
        curr = self.head
        if self.head == None:
            return "Não há aulas para remover"
        else:
            while curr is not None and curr.nome != nome and curr.data != data:
                if curr.nome == nome and curr.data == data:
                    break
                curr = curr.next
            if self.head == self.tail:
                self.head = None
                self.tail = None    
            elif curr == self.head:
                self.head = curr.next
                curr.next.prev = None
            elif curr == self.tail:
                self.tail = curr.prev
                curr.prev.next = None
            else:
                if curr.next is not None:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
    def search(self, nome, data):
        curr = self.head
        while curr is not None:
            if curr.nome == nome and curr.data == data:
                return curr
            curr = curr.next
        return None
    def to_list(self):
        lista = []
        curr = self.head
        while curr:
            lista.append({
                "nome": curr.nome,
                "data": curr.data,
                "inicio": curr.inicio,
                "fim": curr.fim,
                "curso": curr.curso,
                "professor": curr.professor,
                "conteudo": curr.conteudo
            })
            curr = curr.next
        return lista


    