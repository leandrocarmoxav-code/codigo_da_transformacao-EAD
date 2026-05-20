import requests

API_KEY = "SUA_CHAVE_TMDB"

filme = input("Digite o nome do filme: ")

url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={filme}&language=pt-BR"

try:
    resposta = requests.get(url)

    resposta.raise_for_status()

    dados = resposta.json()

    if dados["results"]:

        filme_encontrado = dados["results"][0]

        titulo = filme_encontrado["title"]
        sinopse = filme_encontrado["overview"]
        data = filme_encontrado["release_date"]

        print("\n===== FILME ENCONTRADO =====")
        print(f"Título: {titulo}")
        print(f"Data de lançamento: {data}")
        print(f"Sinopse: {sinopse}")

    else:
        print("Filme não encontrado.")

except requests.exceptions.RequestException as erro:
    print(f"Erro na requisição: {erro}")