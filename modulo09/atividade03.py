import requests

try:
    resposta = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        timeout=5
    )

    resposta.raise_for_status()

    print("Conexão realizada com sucesso!")

except requests.exceptions.ConnectionError:
    print("Sem conexão com a internet.")

except requests.exceptions.Timeout:
    print("Tempo de conexão esgotado.")

except requests.exceptions.HTTPError:
    print("Erro HTTP encontrado.")

except requests.exceptions.RequestException as erro:
    print(f"Erro geral: {erro}")