import os 
import sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__name__))))
import aluno as al
import aula as au
import atividade as at
import json


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
        elif turma.curso < self.head.curso:
            self.head.prev = turma
            turma.next = self.head
            self.head = turma
        elif turma.curso > self.tail.curso:
            self.tail.next = turma
            turma.prev = self.tail
            self.tail = turma
        else:
            while curr is not None and curr.curso <= turma.curso:
                curr = curr.next
            if curr is not None and curr.curso != turma.curso:
                turma.next = curr
                turma.prev = curr.prev
                curr.prev.next = turma
                curr.prev = turma
    def insert_obj(self, turma_obj):
        if self.head == None:
            self.head = turma_obj
            self.tail = turma_obj
        else:
            self.head.prev = turma_obj
            turma_obj.next = self.head
            self.head = turma_obj
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
        while curr is not None:
            if curr.numero == numero and curr.curso == curso:
                return curr
            curr = curr.next
        return None
    def salvar_em_arquivo(self, nome_arquivo):
        data = []
        curr = self.head

        # Converte a lista encadeada em lista normal
        turmas = []
        while curr:
            turmas.append(curr)
            curr = curr.next

        # Ordena pelo atributo 'curso'
        turmas_ordenadas = sorted(turmas, key=lambda t: t.curso)

        # Constrói a lista de dicionários para salvar no JSON
        for t in turmas_ordenadas:
            turma_dict = {
                "numero": t.numero,
                "curso": t.curso,
                "alunos": t.alunos.to_list(),
                "aulas": t.aulas.to_list()
            }
            data.append(turma_dict)

        # Salva no arquivo
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    def ler_de_arquivo(self, arquivo):

        if not os.path.exists(arquivo):
            return

        with open(arquivo, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.head = None
        self.tail = None

        for t_dict in data:
            # Cria o objeto Turma
            turma_obj = Turma(t_dict["numero"], t_dict["curso"])

            # Reconstrói os alunos da turma
            for a_dict in t_dict.get("alunos", []):
                aluno_obj = al.Aluno(a_dict["nome"], a_dict["ra"])
                
                # Reconstrói as atividades do aluno
                for atv_dict in a_dict.get("atividades", []):
                    atv_obj = at.Atividade(atv_dict["nome"], atv_dict["nota"])
                    aluno_obj.atividades.insert_obj(atv_obj)  # Inserção do objeto completo

                # Insere o aluno completo na lista de alunos da turma
                turma_obj.alunos.insert_obj(aluno_obj)

            # Reconstrói as aulas da turma
            for aula_dict in t_dict.get("aulas", []):
                aula_obj = au.Aula(
                    aula_dict["nome"], aula_dict["data"], aula_dict["inicio"],
                    aula_dict["fim"], aula_dict["curso"], aula_dict["professor"],
                    aula_dict["conteudo"]
                )
                turma_obj.aulas.insert_obj(aula_obj)  # Inserção do objeto completo

            # Insere a turma completa na lista de turmas
            self.insert_obj(turma_obj)
        



