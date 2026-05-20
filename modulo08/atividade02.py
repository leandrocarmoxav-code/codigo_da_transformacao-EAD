class SaldoInsuficienteError(Exception):
    pass


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):

        if valor > self.saldo:
            raise SaldoInsuficienteError(
                "Saldo insuficiente para realizar o saque."
            )
        
        self.saldo -= valor

        nome = input("Digite seu nome: ")

        print(f"Saque realizado com sucesso {nome}!")

        print(f"Saldo atual: R${self.saldo}")


conta = ContaBancaria("Lele", 1000)

try:
    valor = float(input("Digite o valor do saque: R$"))
    conta.sacar(valor)

except SaldoInsuficienteError as erro:
    print(f"Erro: {erro}")

except ValueError:
    print("Digite um valor válido.")