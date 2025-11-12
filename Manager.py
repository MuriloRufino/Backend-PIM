from multiprocessing import Manager
import turma as t

def criar_dados_compartilhados():
    manager = Manager()
    dados = manager.Namespace()
    dados.turmas = t.ListaTurmas(manager)  # lista de turmas compartilhada
    return dados