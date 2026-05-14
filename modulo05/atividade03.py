import csv

notas_alunos = [
    ["Nome", "Matemática", "Português"], # Cabeçalho
    ["João", 8.5, 7.0],
    ["Mariana", 9.0, 9.5],
    ["Pedro", 6.0, 7.5]
]

arquivo_csv = "notas_escola.csv"

with open(arquivo_csv, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(notas_alunos)
print("Notas salvas no arquivo CSV com sucesso!")

print("\n--- Lendo o arquivo CSV ---")
with open(arquivo_csv, "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
    
        print(f"{linha[0]:<10} | {linha[1]:<10} | {linha[2]:<10}")