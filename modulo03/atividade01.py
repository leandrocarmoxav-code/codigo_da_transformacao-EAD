lista = []

while True:

    print("\n1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar lista")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        item = input("Digite o item: ")
        lista.append(item)

    elif opcao == "2":

        item = input("Digite o item para remover: ")

        if item in lista:
            lista.remove(item)
        else:
            print("Item não encontrado")

    elif opcao == "3":

        print("Lista de compras:", lista)

    elif opcao == "4":

        print("Programa encerrado")
        break

    else:
        print("Opção inválida")