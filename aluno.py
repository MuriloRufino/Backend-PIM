import atividade as at

class Aluno:
    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra
        self.next = None
        self.prev = None
        self.atividades = at.ListaAtividades()

class ListaAlunos:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, nome, ra):
        curr = self.head
        aluno = Aluno(nome, ra)
        if self.head is None:
            self.head = aluno
            self.tail = aluno
        elif nome < self.head.nome:
            self.head.prev = aluno
            aluno.next = self.head
            self.head = aluno
        elif nome > self.tail.nome:
            self.tail.next = aluno
            aluno.prev = self.tail
            self.tail = aluno
        else:
            while curr.nome < nome:
                curr = curr.next
            if curr.nome != nome:
                aluno.next = curr
                aluno.prev = curr.prev
                curr.prev.next = aluno
                curr.prev = aluno
    def print(self):
        curr = self.head
        print("Deseja mostrar as atividades dos alunos? [S/n]")
        opcao = input()
        print("Alunos:")
        while curr is not None:
            print(curr.nome)
            if(opcao == "S"):
                print("Atividades:")
                curr.atividades.print()
            curr = curr.next
    def remove(self, ra):
        curr = self.head
        if self.head == None:
            return "Lista Vazia"
        else:
            while curr.ra != ra:
                curr = curr.next
            
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
            print("Aluno removido:", curr.nome)
            print("ra:", curr.ra)
    def search(self, ra):
        curr = self.head
        while curr.ra != ra:
            if(curr == self.tail and curr.ra != ra):
                return "Valor não encontrado"
            curr = curr.next
        return curr
        
    
        
