import os
import shutil

pasta_origem = "pasta_importante"
pasta_backup = "backup_seguro"

os.makedirs(pasta_origem, exist_ok=True)
os.makedirs(pasta_backup, exist_ok=True)

with open(f"{pasta_origem}/relatorio.txt", "w") as f:
    f.write("Este é um documento muito importante que precisa de backup.")


print(f"Iniciando backup da pasta '{pasta_origem}' para '{pasta_backup}'...")


arquivos_na_origem = os.listdir(pasta_origem)

for nome_arquivo in arquivos_na_origem:
    caminho_completo_origem = os.path.join(pasta_origem, nome_arquivo)
    

    if os.path.isfile(caminho_completo_origem):
        shutil.copy(caminho_completo_origem, pasta_backup)
        print(f" -> Arquivo '{nome_arquivo}' copiado com sucesso!")

print("Backup concluído!")