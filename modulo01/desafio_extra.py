nome = input("Digite seu nome: ")

print("Olá, " + nome + "! Bem-vindo ao programa")

from datetime import datetime

hora = datetime.now()

print("Hora atual:", hora.strftime("%H:%M"))