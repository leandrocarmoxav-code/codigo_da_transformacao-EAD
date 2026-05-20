import requests

cidade = input("Digite a cidade: ")

api_key = "SUA_CHAVE_API"

url = "https://api.openweathermap.org/data/2.5/weather?q=" + cidade + "&appid=" + api_key + "&units=metric&lang=pt_br"

try:
    resposta = requests.get(url)

    dados = resposta.json()

    print("\n===== CLIMA =====")
    print("Cidade:", cidade)
    print("Temperatura:", dados["main"]["temp"], "°C")
    print("Clima:", dados["weather"][0]["description"])

except Exception as erro:
    print("Erro:", erro)