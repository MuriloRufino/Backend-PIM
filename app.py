import turma as t
import importlib
import subprocess


def cadastro_login(nome, credencial, senha):
    mod = importlib.import_module(nome)
    if(mod.login(credencial, senha) == False):
        opcao = input("Login inválido, deseja fazer o cadastro?[S/n]")
        if(opcao == "S"):
            mod.cadastro(credencial, senha)
            return True
        return False
    
    mod.login(credencial, senha)
    return True


credencial = input("Insira sua credencial e senha\n")
senha = input()
if cadastro_login("inicio", credencial, senha):
    turma = t.ListaTurmas()
    print("O que deseja fazer?\n1 - Inserir turmas\n2 - Consultar turmas\n3 - Buscar turma\n4 - Remover turma")
    print("5 - Inserir novos alunos em uma turma\n6 - Consultar alunos de uma turma\n6 - Buscar aluno de uma turma\n7 - Remover aluno de uma turma\n8 - Inserir novas atividades para um aluno")
    print("9 - Consultar atividades de um aluno\n10 - Buscar atividade de um aluno\n11 - Remover atividade de um aluno\n12 - Inserir aulas em uma turma\n13 - Consultar aulas de uma turma")
    print("14 - Buscar aula de uma turma\n15 - Remover aula de uma turma\nOutro - Trocar mensagens (Diário eletrônico e chat)")

    opcao = int(input())
    while opcao >= 1 and opcao <= 15:
        if opcao == 1:
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma.insert(numero, curso)
        elif opcao == 2:
            turma.print()
        elif opcao == 3:
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            print("Turma encontrada:\n")
            print("Numero:", numero)
            print("Curso:", curso)
            turma1.alunos.print()
        elif opcao == 4:
            numero = int(input("Insira o número da turma\n"))
            turma.remove(numero)
        elif opcao == 5:
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            nome = input("Insira o nome, RA e atividades do aluno, se houver\n")
            ra = input()
            turma1.alunos.insert(nome, ra)
        elif opcao == 6:
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            nome = input("Insira o nome do aluno\n")
            turma1.alunos.search(nome)
        elif opcao == 7:    
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            nome = input("Insira o nome do aluno\n")
            turma1.alunos.remove(nome)
        elif opcao == 8:
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            ra = input("Insira o RA do aluno\n")
            aluno = turma1.alunos.search(ra)
            nome = input("Insira o nome e nota da atividade\n")
            nota = input()
            aluno.atividades.insert(nome)
        elif opcao == 9:
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            ra = input("Insira o RA do aluno\n")
            aluno = turma1.alunos.search(ra)
            aluno.atividades.print()
        elif opcao == 10:
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            ra = input("Insira o RA do aluno\n")
            aluno = turma1.alunos.search(ra)
            nome = input("Insira o nome da atividade")
            aluno.atividades.search(nome)
        elif opcao == 11:
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            ra = input("Insira o RA do aluno\n")
            aluno = turma1.alunos.search(ra)
            nome = input("Insira o nome da atividade")
            aluno.atividades.remove(nome)
        elif opcao == 12:    
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            nome = input("Insira os dados:\nNome da aula\n")
            inicio = input("Hora de início:\n")
            fim = input("Hora do fim:\n")
            professor = input("Nome do professor:\n")
            conteudo = input("Conteudo da aula:\n")
            turma1.aulas.insert(nome, inicio, fim, curso, professor, conteudo)
        elif opcao == 13:    
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            turma1.aulas.print()
        elif opcao == 14:    
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            nome = input("Insira o nome da aula")
            turma1.aulas.search(nome)
        elif opcao == 15:    
            numero = int(input("Insira o número e o curso da turma\n"))
            curso = input()
            turma1 = turma.search(numero, curso)
            nome = input("Insira o nome da aula\n")
            turma1.aulas.remove(nome, curso)

            
                        
        
        
        print("O que deseja fazer?\n1 - Inserir turmas\n2 - Consultar turmas\n3 - Buscar turma\n4 - Remover turma")
        print("5 - Inserir novos alunos em uma turma\n6 - Consultar alunos de uma turma\n6 - Buscar aluno de uma turma\n7 - Remover aluno de uma turma\n8 - Inserir novas atividades para um aluno")
        print("9 - Consultar atividades de um aluno\n10 - Buscar atividade de um aluno\n11 - Remover atividades de um aluno\n12 - Inserir aulas em uma turma\n13 - Consultar aulas de uma turma")
        print("14 - Buscar aula de uma turma\n15 - Remover aula de uma turma\nOutro - Trocar mensagens (Diário eletrônico e chat)")
        opcao = int(input("Para sair do menu, digite um número não disponível nas opções, você será direcionado ao chat entre usuários\n"))

    subprocess.run(["./cliente"])

