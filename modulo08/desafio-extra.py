usuario_correto = "admin"
senha_correta = "1234"

tentativas = 3

while tentativas > 0:

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    try:

        if usuario != usuario_correto or senha != senha_correta:
            raise ValueError("Usuário ou senha inválidos!")

        print("\nLogin realizado com sucesso!")
        break

    except ValueError as erro:
        tentativas -= 1

        print(f"\nErro: {erro}")
        print(f"Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("\nConta bloqueada por excesso de tentativas.")