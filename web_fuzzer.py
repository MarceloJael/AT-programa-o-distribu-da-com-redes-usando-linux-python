import requests

alvo = input("Digite a URL do servidor (ex: http://localhost:8080): ")

# Lista de caminhos para fuzzing
wordlist = ["admin", "login", "test", "backup", "config", "dashboard", "hidden", "panel"]

print(f"\n🚀 Iniciando fuzzing em {alvo}...\n")

for palavra in wordlist:
    url = f"{alvo}/{palavra}"
    try:
        resposta = requests.get(url, timeout=3)
        status = resposta.status_code
        if status in [200, 301, 302, 403]:
            print(f"🔍 {url} → Status: {status} (possível rota válida)")
        else:
            print(f"✖️ {url} → Status: {status}")
    except:
        print(f"⚠️ {url} → Erro na requisição")

