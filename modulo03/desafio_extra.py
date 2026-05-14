agenda = {}

while True:

    print("\n1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Remover contato")
    print("4 - Mostrar agenda")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Nome: ")
        telefone = input("Telefone: ")

        agenda[nome] = telefone

    elif opcao == "2":

        nome = input("Digite o nome: ")

        if nome in agenda:
            print("Telefone:", agenda[nome])

        else:
            print("Contato não encontrado")

    elif opcao == "3":

        nome = input("Digite o nome para remover: ")

        if nome in agenda:
            del agenda[nome]
            print("Contato removido")

        else:
            print("Contato não encontrado")

    elif opcao == "4":

        print(agenda)
        print("Agenda completa:", agenda)

    elif opcao == "5":

        print("Programa encerrado")
        break

    else:
        print("Opção inválida")