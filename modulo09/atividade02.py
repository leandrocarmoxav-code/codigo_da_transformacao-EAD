import requests

API_KEY = "SUA_CHAVE_API"

cidade = "São Paulo"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    resposta = requests.get(url)
    dados = resposta.json()

    print("\n===== DADOS CLIMÁTICOS =====")
    print(f"Temperatura atual: {dados['main']['temp']}°C")
    print(f"Sensação térmica: {dados['main']['feels_like']}°C")
    print(f"Clima: {dados['weather'][0]['description']}")
    print(f"Velocidade do vento: {dados['wind']['speed']} m/s")

except Exception as erro:
    print(f"Erro: {erro}")