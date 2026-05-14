nome = input("Digite o seu nome: ")

print("Olá, " + nome + "! Bem-Vindo ao programa, estes são os números pares e ímpares de 1 a 10:")



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Números pares:")

for numero in numeros:

    if numero % 2 == 0:
        print(numero)

print("Números ímpares:")

for numero in numeros:

    if numero % 2 != 0:
        print(numero)