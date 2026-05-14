import random
import math

numero_secreto = random.randint(1, 100)

tentativa = int(input("Adivinhe o numero entre 1 e 100: "))

diferenca = abs(numero_secreto - tentativa)

if tentativa == numero_secreto:
    print("Parabéns! Você acertou o número secreto!")
else:
    print("Que pena! Você errou o número secreto.")
    print(f"O número secreto era {numero_secreto}")
