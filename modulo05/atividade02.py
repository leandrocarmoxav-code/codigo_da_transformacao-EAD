import json

clientes = {
    "cliente_01": {"nome": "Ana Souza", "idade": 28, "cidade": "São Paulo"},
    "cliente_02": {"nome": "Carlos Silva", "idade": 35, "cidade": "Rio de Janeiro"}
}

nome_arquivo = "dados_clientes.json"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
print("Dicionário salvo em JSON com sucesso!")


print("\n--- Lendo o arquivo JSON ---")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)
    
    for chave, info in dados_carregados.items():
        print(f"ID: {chave} | Nome: {info['nome']} | Cidade: {info['cidade']}")