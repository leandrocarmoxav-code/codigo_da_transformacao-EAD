'''

Crud

'''

def realizar_login_com_tentativas():
    """
    Função de login que permite até 3 tentativas antes de bloquear.
    """

    senha_padrao = "vocacao2025"
    tentativas_restantes = 3
    login_sucesso = False 

    print("\n--- Sistema de Login (Máx. 3 Tentativas) ---")
    nome_usuario = input("Digite seu login: ")

    
    while tentativas_restantes > 0 and not login_sucesso:
        print(f"\nTentativas restantes: {tentativas_restantes}")
        senha_digitada = getpass.getpass("Digite sua senha: ")

        if senha_digitada == senha_padrao:
            print(f"\n[SUCESSO] Bem-vindo, {nome_usuario}!")
            login_sucesso = True  #
        else:
            tentativas_restantes -= 1
            if tentativas_restantes > 0:
                print("[ERRO] Senha incorreta. Tente novamente.")
            else:
                print("\n[BLOQUEADO] Número de tentativas excedido!")

    print("--- Fim da Operação ---")


realizar_login_com_tentativas()