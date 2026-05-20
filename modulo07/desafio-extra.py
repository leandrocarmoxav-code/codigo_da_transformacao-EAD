class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} | {self.autor} | {self.ano} | {status}"


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"\nLivro '{livro.titulo}' adicionado com sucesso!")

   
    def listar_livros(self):
        print(f"\n===== LIVROS DA {self.nome.upper()} =====")

        if len(self.livros) == 0:
            print("Nenhum livro cadastrado.")
            return

        for i, livro in enumerate(self.livros, start=1):
            print(f"{i}. {livro}")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():

                if livro.disponivel:
                    livro.disponivel = False
                    print(f"\nLivro '{livro.titulo}' emprestado com sucesso!")
                else:
                    print(f"\nO livro '{livro.titulo}' já está emprestado.")

                return

        print("\nLivro não encontrado.")

  
    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():

                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"\nLivro '{livro.titulo}' devolvido com sucesso!")
                else:
                    print(f"\nO livro '{livro.titulo}' já estava disponível.")

                return

        print("\nLivro não encontrado.")


    def buscar_livro(self, titulo):
        for livro in self.livros:
            if titulo.lower() in livro.titulo.lower():
                print("\nLivro encontrado:")
                print(livro)
                return

        print("\nLivro não encontrado.")

biblioteca = Biblioteca("Central dos Livros")

biblioteca.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis", 1899))
biblioteca.adicionar_livro(Livro("Harry Potter", "J.K Rowling", 1997))
biblioteca.adicionar_livro(Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943))

while True:

    print("\n======= MENU =======")
    print("1 - Listar livros")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Buscar livro")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        biblioteca.listar_livros()

    elif opcao == "2":
        titulo = input("Digite o nome do livro: ")
        biblioteca.emprestar_livro(titulo)

    elif opcao == "3":
        titulo = input("Digite o nome do livro: ")
        biblioteca.devolver_livro(titulo)

    elif opcao == "4":
        titulo = input("Digite o nome do livro: ")
        biblioteca.buscar_livro(titulo)

    elif opcao == "5":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida.")