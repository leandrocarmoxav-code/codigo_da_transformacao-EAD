
texto_para_salvar = "Olá! Esta é a minha primeira linha no arquivo.\nE esta é a segunda linha de teste."

with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_para_salvar)
print("Arquivo .txt criado e dados gravados com sucesso!")

print("\n--- Lendo o conteúdo do arquivo ---")
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteudo_lido = arquivo.read()
    print(conteudo_lido)