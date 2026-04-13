'''





'''

# ======================================================================
# 🚀 Projeto: Minha Primeira Função
# ======================================================================


def saudacao(nome):
    print(f"Olá, {nome}! Que bom te ver por aqui.")


print("--- Chamando a função 'saudacao' ---")


saudacao("João")


saudacao("Maria")


meu_nome = "Parceiro de Programação"
saudacao(meu_nome)

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================

'''

'''

# ======================================================================
# 🚀 Projeto: Encontrar o Maior e o Menor Valor
# ======================================================================


def maior_menor(lista_de_numeros):
    
    if not lista_de_numeros:
        return None, None

    
    maior_valor = max(lista_de_numeros)
    menor_valor = min(lista_de_numeros)
    
    
    return maior_valor, menor_valor

print("--- Teste com uma lista de números ---")
numeros = [12, 5, 25, 8, 17, 3, 30]



print(f"A lista de números é: {numeros}")
print(f"O maior valor na lista é: {maior}")
print(f"O menor valor na lista é: {menor}")

print("\n--- Teste com uma lista vazia ---")
lista_vazia = []
maior_vazio, menor_vazio = maior_menor(lista_vazia)

print(f"A lista é: {lista_vazia}")
print(f"Maior valor: {maior_vazio}, Menor valor: {menor_vazio}")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================