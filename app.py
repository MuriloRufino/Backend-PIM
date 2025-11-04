import turma as t
turma = t.ListaTurmas()
print("O que deseja fazer?\n1 - Inserir turmas\n2 - Consultar turmas\n3 - Buscar turma\n4 - Remover turma")
print("5 - Inserir novos alunos em uma turma\n6 - Buscar aluno de uma turma\n7 - Remover aluno de uma turma\n8 - Inserir aulas em uma turma")
print("9 - Consultar aulas de uma turma\n10 - Buscar aula de uma turma\n11 - Remover aula de uma turma")

opcao = int(input())
while opcao >= 1 and opcao <= 11:
    if opcao == 1:
        numero = int(input("Insira o número e o curso da turma\n"))
        curso = input()
        turma.insert(numero, curso)
    elif opcao == 2:
        turma.print()
    elif opcao == 3:
        numero = int(input("Insira o número e o curso da turma\n"))
        curso = input()
        turma.search(numero, curso)
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
        nome = input("Insira o nome, horario, e professor da aula\n")
        horario = input()
        professor = input()
        turma1.aulas.insert(nome, horario, curso, professor)
    elif opcao == 9:    
        numero = int(input("Insira o número e o curso da turma\n"))
        curso = input()
        turma1 = turma.search(numero, curso)
        turma1.aulas.print()
    elif opcao == 10:    
        numero = int(input("Insira o número e o curso da turma\n"))
        curso = input()
        turma1 = turma.search(numero, curso)
    elif opcao == 11:    
        numero = int(input("Insira o número e o curso da turma\n"))
        curso = input()
        turma1 = turma.search(numero, curso)
        nome = input("Insira o nome da aula\n")
        turma1.aulas.remove(nome, curso)
    
    print("O que deseja fazer?\n1 - Inserir turmas\n2 - Consultar turmas\n3 - Buscar turma\n4 - Remover turma")
    print("5 - Inserir novos alunos em uma turma\n6 - Buscar aluno de uma turma\n7 - Remover aluno de uma turma\n8 - Inserir aulas em uma turma")
    print("9- Consultar aulas de uma turma\n10 - Buscar aula de uma turma\n11 - Remover aula de uma turma\n12 - Trocar mensagens")
    opcao = int(input("Para sair do menu, digite um número não disponível nas opções, você será direcionado ao chat entre usuários\n"))
    