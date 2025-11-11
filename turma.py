import os 
import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__name__))))
import aluno as al
import aula as au


class Turma:
    def __init__(self, numero, curso):
        self.next = None
        self.prev = None
        self.numero = numero
        self.curso = curso
        self.alunos = al.ListaAlunos()
        self.aulas = au.ListaAulas()
    
class ListaTurmas:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, numero, curso):
        curr = self.head
        turma = Turma(numero, curso)
        if self.head is None:
            self.head = turma
            self.tail = turma
        elif curso < self.head.curso:
            self.head.prev = turma
            turma.next = self.head
            self.head = turma
        elif curso > self.tail.curso:
            self.tail.next = turma
            turma.prev = self.tail
            self.tail = turma
        else:
            while curr.curso <= curso:
                curr = curr.next
            if curr.curso != curso:
                turma.next = curr
                turma.prev = curr.prev
                curr.prev.next = turma
                curr.prev = turma
    def print(self):
        curr = self.head
        while curr is not None:
            print("Numero da turma:", curr.numero)
            print("Curso:", curr.curso)
            curr.alunos.print()
            curr = curr.next
    
        
    def remove(self, numero):
        curr = self.head
        if self.head == None:
            return "Não há turmas para remover"
        else:
            while curr.numero != numero:
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
            print("Numero e curso da turma removida:", curr.numero, curr.curso)
    def search(self, numero, curso):
        curr = self.head
        while curr.numero != numero and curr.curso != curso:
            if(curr == self.tail and curr.numero != numero and curr.curso != curso):
                return "Turma não encontrada"
            curr = curr.next
        return curr
       
    
    



