usuarios = {

    "leandro": "1234",
    "admin": "admin"
}

def login(usuario, senha):

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso")

    else:
        print("Usuário ou senha incorretos tente novamente")

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

login(usuario, senha)