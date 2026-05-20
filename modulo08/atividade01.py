try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 / num2

    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    print("Erro: não é possível dividir por zero!")

except ValueError:
    print("Erro: digite apenas números.")