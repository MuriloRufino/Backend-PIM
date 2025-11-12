class Atividade:
    def __init__(self, nome, nota):
        self.next = None
        self.prev = None
        self.nome = nome
        self.nota = nota

class ListaAtividades:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, nome, nota = 0):
        curr = self.head
        atividade = Atividade(nome, nota)
        if self.head is None:
            self.head = atividade
            self.tail = atividade
        elif nome < self.head.nome:
            self.head.prev = atividade
            atividade.next = self.head
            self.head = atividade
        elif nome > self.tail.nome:
            self.tail.next = atividade
            atividade.prev = self.tail
            self.tail = atividade
        else:
            while curr.nome < nome:
                curr = curr.next
            if curr.nome != nome:
                atividade.next = curr
                atividade.prev = curr.prev
                curr.prev.next = atividade
                curr.prev = atividade
    def insert_obj(self, atividade_obj):
        if self.head == None:
            self.head = atividade_obj
            self.tail = atividade_obj
        else:
            self.head.prev = atividade_obj
            atividade_obj.next = self.head
            self.head = atividade_obj

    def print(self):
        curr = self.head
        while curr is not None:
            print(curr.nome)
            print("Nota: ", curr.nota)
            curr = curr.next
    
    def remove(self, atividade):
        curr = self.head
        if self.head == None:
            return "Lista Vazia"
        else:
            while curr.atividade != atividade:
                curr = curr.next
            print("", curr.atividade)
            
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
                    
    def search(self, nome):
        curr = self.head
        while curr is not None:
            if curr.nome == nome:
                return curr
            curr = curr.next
        return None
    
    def atualizar_nota(self, nome, nota):
        curr = self.head
        while curr.nome != nome:
            if(curr == self.tail and curr.nome != nome):
                return "Atividade não encontrada"
            curr = curr.next
        curr.nota = nota
    def to_list(self):
        lista = []
        curr = self.head
        while curr:
            lista.append({
                "nome": curr.nome,
                "nota": curr.nota
            })
            curr = curr.next
        return lista

    
    def from_list(cls, lista_dados):
        obj = cls()
        for dado in lista_dados:
            obj.insert(dado["nome"], dado["nota"])
        return obj