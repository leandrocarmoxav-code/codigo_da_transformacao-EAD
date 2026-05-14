while True:

    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))

        print("Resultado:", n1 + n2)

    elif opcao == "2":

        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))

        print("Resultado:", n1 - n2)

    elif opcao == "3":

        print("Programa encerrado")
        break

    else:
        print("Opção inválida")